import collections
import inspect
import itertools
import math
import sys
import typing
import utilitools

IterType = typing.TypeVar('IterType', bound=typing.Callable[[typing.Iterator], typing.Any])
ReturnAnnotation = typing.TypeVar('ReturnAnnotation', typing.Any, typing.Sequence[typing.Any])


class Subscription:
    def __init__(self, func, iter_type):
        self._func = func
        self._type = iter_type

    def __getitem__(self, key):
        if isinstance(key, int):
            if inspect.isgeneratorfunction(self._func):
                iterable = self._func()
                iterator = utilitools.islice(iterable, key + 1)
            else:
                iterable = map(self._func, itertools.count(key))
                iterator = utilitools.islice(iterable, 1)
            return collections.deque(iterator, 1).pop()
        if isinstance(key, slice):
            key = self.numeric_slice(key)
            if inspect.isgeneratorfunction(self._func):
                iterable = self._func()
                iterator = utilitools.islice(iterable, key.start, key.stop, key.step)
            else:
                iterable = map(self._func, itertools.count(key.start, key.step))
                iterator = utilitools.islice(iterable, math.ceil((key.stop - key.start) / key.step))
            return self._type(iterator) if self._type is not None else iterator

    @staticmethod
    def numeric_slice(key):
        if key.step is None or key.step > 0:
            return slice(
                0 if key.start is None else key.start,
                sys.maxsize if key.stop is None else key.stop,
                1 if key.step is None else key.step,
            )
        elif key.step < 0:
            return slice(
                sys.maxsize if key.start is None else key.start,
                -sys.maxsize if key.stop is None else key.stop,
                -1 if key.step is None else key.step,
            )
        else:
            return slice(0, 0, 0)


def subscriptable(iter_type: IterType = None, /) -> ReturnAnnotation:
    """
    A decorator that transforms a function into a subscription object.

    :param iter_type:
        | Declaration of the returned data type while the kind of key is ``slice``.
        | By default, returned ``utilitools.islice``.
    :return:
        | The returned value depends on the key.
        | A single value while the kind of key is ``int``.
        | Multiple values while the kind of key is ``slice``.
    """
    def wrapper(func):
        return Subscription(func, iter_type)
    return wrapper
