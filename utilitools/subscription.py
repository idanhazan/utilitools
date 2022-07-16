import collections
import inspect
import itertools
import math
import sys
import utilitools


class Subscription:
    def __init__(self, func, type):
        self._func = func
        self._type = type

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
        if key.step is None or key.step >= 0:
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
            return key


def subscription(type=None, /):
    """
    | Transforms a function into a subscription object.

    | Subscription is applicable on:
    - Functions that accept one positional argument.
    - Generators that do not accept arguments at all.

    .. note::
        | In both cases, they must behave as a sequence.

    :param type:
        | The returned data type when the `key` is `slice`.
        | By default, returned :obj:`utilitools.islice`.
    :type type: `callable[iterator]`, default `None`
    :return: A subscription object that already implements the `__getitem__` magic method.
    :rtype: :obj:`utilitools.subscription.Subscription`
    :raises TypeError:
        - If `type` is not a `callable` that accepts an `iterator`.
        - If the `function` does not accept one positional argument.
        - If the `generator` accepts at least one argument.
        - If the `key` is not `int` or `slice`.
    """
    def wrapper(func):
        return Subscription(func, type)
    return wrapper
