import collections
import inspect
import itertools
import math
import sys
import utilitools


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
        ltr = slice(0, sys.maxsize, 1)
        rtl = slice(sys.maxsize, -sys.maxsize, -1)
        if key.step < 0:
            return slice(
                rtl.start if key.start is None else key.start,
                rtl.stop if key.stop is None else key.stop,
                rtl.step if key.step is None else key.step,
            )
        else:
            return slice(
                ltr.start if key.start is None else key.start,
                ltr.stop if key.stop is None else key.stop,
                ltr.step if key.step is None else key.step,
            )


def subscription(iter_type=None, /):
    """
    | A decorator that transforms a function into a subscription object.

    .. note::
        | A subscription object (in Python) means it implements the ``__getitem__(self, key)`` magic method.
        | test1: :obj:`__getitem__`
        | test2: :object:`__getitem__`
        | test3: :func:`__getitem__`

    | Subscription is a private case of function use (valid for a situation where the function behaves like a sequence).
    | When needed, the code will be more readable and will also make it easier to write in a "pythonic" style.

    :param iter_type:
        | The returned data type when `key` is :func:`slice`.
        | By default, returned :func:`utilitools.islice`.
    :type iter_type: callable[iterator], default `None`
    :return: A subscription object that already implements the `__getitem__` magic method.
    :rtype: :class:`utilitools.subscription.Subscription`
    """
    def wrapper(func):
        return Subscription(func, iter_type)
    return wrapper
