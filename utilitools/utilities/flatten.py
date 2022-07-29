import itertools


def flatten(iterable, /, *, dictionaries='keys', levels=None, types=None):
    """
    | Flatten an iterable with multiple levels of nesting.

    :param iterable:
        | Iterable to be flattened.
    :type iterable: collections.Iterable

    :param dictionaries:
        | The way iterates over dictionaries.
        | The possible options are `items`, `keys`, and `values`.
        | By default, it will iterate on `keys`.
    :type dictionaries: str

    :param levels:
        | Nesting levels we want to flatten in the iterator.
        | By default, will be set to `flaot('inf')`.
    :type levels: int

    :param types:
        | Base types that we will not refer to in flattening.
        | By default, both `bytes` and `str` are predefined.
    :type types: tuple[type]

    :return: An iterator with flatten items.
    :rtype: collections.Iterator
    """
    levels = float('inf') if levels is None else levels
    types = (bytes, str) if types is None else (bytes, str) + types

    def recursive_flatten(item, level):
        if level > levels or isinstance(item, types) or not hasattr(item, '__iter__'):
            yield item
        elif isinstance(item, dict):
            if dictionaries == 'items':
                for item in itertools.chain(*item.items()):
                    yield from recursive_flatten(item, level + 1)
            elif dictionaries in ['keys', 'values']:
                for item in getattr(item, dictionaries)():
                    yield from recursive_flatten(item, level + 1)
        else:
            for item in iter(item):
                yield from recursive_flatten(item, level + 1)

    yield from recursive_flatten(iterable, 0)
