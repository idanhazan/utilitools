import collections
import inspect
import itertools
import math
import sys


class Subscription:
    def __init__(self, func, iter_type):
        self._func = func
        self._type = iter_type

    def __getitem__(self, key):
        if isinstance(key, int):
            if inspect.isgeneratorfunction(self._func):
                iterable = self._func()
                iterator = itertools.islice(iterable, key + 1)
            else:
                iterable = map(self._func, itertools.count(key))
                iterator = itertools.islice(iterable, 1)
            return collections.deque(iterator, 1).pop()
        if isinstance(key, slice):
            key = slice(
                0 if key.start is None else key.start,
                sys.maxsize if key.stop is None else key.stop,
                1 if key.step is None else key.step,
            )
            if inspect.isgeneratorfunction(self._func):
                iterable = self._func()
                iterator = itertools.islice(iterable, key.start, key.stop, key.step)
            else:
                iterable = map(self._func, itertools.count(key.start, key.step))
                iterator = itertools.islice(iterable, math.ceil((key.stop - key.start) / key.step))
            return self._type(iterator) if self._type is not None else iterator


def subscriptable(iter_type=None, /):
    """
    A decorator that transforms a function into a subscription object.

    :param iter_type:
        The type of data structure returned from the function when ``isinstance(key, slice)``,
        the default is ``itertools.islice``.
    :return:
        The returned value depends on the ``key``,
        for ``isinstance(key, int)`` no change will be made and
        for ``isinstance(key, slice)`` the values will be wrapped by ``iter_type``,
        otherwise ``None`` will be returned.
    """
    def wrapper(func):
        return Subscription(func, iter_type)
    return wrapper
