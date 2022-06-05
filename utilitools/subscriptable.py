import collections
import inspect
import itertools
import math
import sys


class Sequence:
    def __init__(self, func, dtype):
        self.func = func
        self.dtype = dtype

    def __getitem__(self, key):
        if isinstance(key, int):
            if inspect.isgeneratorfunction(self.func):
                iterable = self.func()
                iterator = itertools.islice(iterable, key + 1)
            else:
                iterable = map(self.func, itertools.count(key))
                iterator = itertools.islice(iterable, 1)
            return collections.deque(iterator, 1).pop()
        if isinstance(key, slice):
            key = slice(
                0 if key.start is None else key.start,
                sys.maxsize if key.stop is None else key.stop,
                1 if key.step is None else key.step,
            )
            if inspect.isgeneratorfunction(self.func):
                iterable = self.func()
                iterator = itertools.islice(iterable, key.start, key.stop, key.step)
            else:
                iterable = map(self.func, itertools.count(key.start, key.step))
                iterator = itertools.islice(iterable, math.ceil((key.stop - key.start) / key.step))
            return self.dtype(iterator) if self.dtype else iterator


def subscriptable(dtype=None):
    def wrapper(func):
        return Sequence(func, dtype)
    return wrapper
