import collections
import itertools
import operator
import sys


def islice(iterable, *args):
    """
    | Make an iterator that returns selected elements from an iterable.

    | An extension of |itertools.islice| that supports negative values for `start`, `stop`, and `step`.
    | In some cases, negative values require caching,
      this function takes care to minimize the amount of memory required.

    .. warning::
        | Infinite caching can lead to memory issues.

    :param iterable:
        | Iterable to which the slice object will be applied.
    :type iterable: `iterable[any]`
    :param args:
        | Arguments for slice object:
        - `stop`
        - `start`, `stop`
        - `start`, `stop`, `step`
    :type args: `optional[int]`
    :return: An iterator with the selected elements.
    :rtype: :obj:`utilitools.islice`
    :raises TypeError:
        - If `iterable` is not iterable.
        - If `args` is empty or contains more than three arguments.
        - If `args` values are not comparable (except `NoneType`).
    :raises ValueError:
        - If `args` values are not `NoneType` or `int`.
        - If `step` (from `args`) is equal to zero.
    """
    iterator = iter(iterable)
    key = slice(*args)
    step = 1 if key.step is None else key.step
    length = max(getattr(iterable, '__len__', lambda: -1)(), getattr(iterable, '__length_hint__', lambda: -1)())
    if step >= 0 and length >= 0:
        start = 0 if key.start is None else key.start
        stop = length if key.stop is None else key.stop
        start = length + start if start < 0 else start
        stop = length + stop if stop < 0 else stop
        yield from itertools.islice(iterable, start, stop, step)
    elif step < 0 and length >= 0 and hasattr(iterable, '__reversed__'):
        start = -1 if key.start is None else key.start
        stop = -length if key.stop is None else key.stop
        start = length - (length + start) - 1 if start < 0 else length - start - 1
        stop = length - (length + stop) - 1 if stop < 0 else length - stop - 1
        yield from itertools.islice(reversed(iterable), start, stop, -step)
    elif step >= 0:
        start = 0 if key.start is None else key.start
        stop = sys.maxsize if key.stop is None else key.stop
        if start >= 0 and stop >= 0:
            yield from itertools.islice(iterable, start, stop, step)
        elif start >= 0 and stop < 0:
            cache = collections.deque(itertools.islice(iterator, start, None))
            stop = len(cache) + stop
            if stop > 0:
                yield from itertools.islice(cache, 0, stop, step)
        elif start < 0 and stop >= 0:
            cache = collections.deque(enumerate(iterator, 1), -start)
            iterable = map(operator.itemgetter(1), cache)
            length = cache[-1][0] if cache else 0
            stop = min(length, stop) - max(0, length + start)
            if stop > 0:
                yield from itertools.islice(iterable, 0, stop, step)
        elif start < 0 and stop < 0 and start < stop:
            cache = collections.deque(iterator, -start)
            stop = len(cache) + stop
            yield from itertools.islice(cache, 0, stop, step)
    elif step < 0:
        start = sys.maxsize if key.start is None else key.start
        stop = -sys.maxsize if key.stop is None else key.stop
        if start >= 0 and stop >= 0 and start > stop:
            start, stop = min(sys.maxsize, stop + 1), min(sys.maxsize, start + 1)
            cache = collections.deque(itertools.islice(iterator, start, stop))
            yield from itertools.islice(reversed(cache), 0, None, -step)
        elif start >= 0 and stop < 0:
            cache = collections.deque(enumerate(iterator, 1), -stop - 1)
            iterable = map(operator.itemgetter(1), reversed(cache))
            length = cache[-1][0] if cache else 0
            start = max(0, length - start - 1)
            yield from itertools.islice(iterable, start, None, -step)
        elif start < 0 and stop >= 0:
            cache = collections.deque(enumerate(iterator, 1))
            iterable = map(operator.itemgetter(1), reversed(cache))
            length = cache[-1][0] if cache else 0
            start = -start - 1
            stop = length - stop - 1
            if stop - start >= 0:
                yield from itertools.islice(iterable, start, stop, -step)
        elif start < 0 and stop < 0 and start > stop:
            cache = collections.deque(iterator, -stop - 1)
            start = -start - 1
            yield from itertools.islice(reversed(cache), start, None, -step)
