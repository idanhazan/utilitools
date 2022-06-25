import collections
import inspect
import itertools
import math
import sys
import typing


class Subscription:
    def __init__(self, func, sliced_type):
        self._func = func
        self._type = sliced_type

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


def subscriptable(sliced_type: typing.Any = None, /) -> typing.Callable[[typing.Any], Subscription]:
    """
    A decorator that transforms a function into a subscription object.

        >>> from utilitools import subscriptable

        >>> @subscriptable(tuple)
        >>> def digital_sum(n):
        >>>    return sum(map(int, str(n)))

        >>> @subscriptable(list)
        >>> def fibonacci():
        >>>     a, b = 0, 1
        >>>     yield a
        >>>     while True:
        >>>        a, b = b, a + b
        >>>         yield a

        >>> digital_sum[123]
        6
        >>> digital_sum[10:20:3]
        (1, 4, 7, 10)
        >>> fibonacci[123]
        22698374052006863956975682
        >>> fibonacci[10:20:3]
        [55, 233, 987, 4181]

    :param sliced_type:
        Slicing can yield more than one value,
        and you can choose the return type by passing `list` or `tuple` or any else.
        By default, return an `itertools.islice` object.
    :return:
        A subscription object.
    """
    def wrapper(func):
        return Subscription(func, sliced_type)
    return wrapper
