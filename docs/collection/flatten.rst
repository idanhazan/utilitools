flatten
=======

.. autofunction:: utilitools.flatten

Examples
--------

.. code-block:: python

    from utilitools import flatten

    iterable = [1, [2, (3, 4), 5], 6, (7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8), 9]

Flattening an iterable while dictionaries are unpacking by `items`:

>>> list(flatten(iterable, dictionaries='items'))
[1, 2, 3, 4, 5, 6, 7, 'a', 10, 20, 'a1', 30, 40, 'b', 50, 8, 9]

Flattening an iterable while dictionaries are unpacking by `keys`:

>>> list(flatten(iterable, dictionaries='keys'))
[1, 2, 3, 4, 5, 6, 7, 'a', 'b', 8, 9]

Flattening an iterable while dictionaries are unpacking by `values`:

>>> list(flatten(iterable, dictionaries='values'))
[1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 8, 9]

Flattening an iterable while dictionaries are define as base type:

>>> list(flatten(iterable, types=(dict,)))
[1, 2, 3, 4, 5, 6, 7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8, 9]

Flattening an iterable while tuples are define as base type:

>>> list(flatten(iterable, types=(tuple,)))
[1, 2, (3, 4), 5, 6, (7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8), 9]

Flattening an iterable by `K` nesting level:

>>> list(flatten(iterable, levels=1))
[1, 2, (3, 4), 5, 6, 7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8, 9]

>>> list(flatten(iterable, levels=2))
[1, 2, 3, 4, 5, 6, 7, 'a', 'b', 8, 9]

Flattening an iterable by `K` nesting level while dictionaries are unpacking by `items`:

>>> list(flatten(iterable, levels=1, dictionaries='items'))
[1, 2, (3, 4), 5, 6, 7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8, 9]

>>> list(flatten(iterable, levels=2, dictionaries='items'))
[1, 2, 3, 4, 5, 6, 7, 'a', [10, (20, {'a1': 30}), 40], 'b', 50, 8, 9]

>>> list(flatten(iterable, levels=3, dictionaries='items'))
[1, 2, 3, 4, 5, 6, 7, 'a', 10, (20, {'a1': 30}), 40, 'b', 50, 8, 9]

>>> list(flatten(iterable, levels=4, dictionaries='items'))
[1, 2, 3, 4, 5, 6, 7, 'a', 10, 20, {'a1': 30}, 40, 'b', 50, 8, 9]

>>> list(flatten(iterable, levels=5, dictionaries='items'))
[1, 2, 3, 4, 5, 6, 7, 'a', 10, 20, 'a1', 30, 40, 'b', 50, 8, 9]

Flattening an iterable by `K` nesting level while dictionaries are unpacking by `values`:

>>> list(flatten(iterable, levels=1, dictionaries='values'))
[1, 2, (3, 4), 5, 6, 7, {'a': [10, (20, {'a1': 30}), 40], 'b': 50}, 8, 9]

>>> list(flatten(iterable, levels=2, dictionaries='values'))
[1, 2, 3, 4, 5, 6, 7, [10, (20, {'a1': 30}), 40], 50, 8, 9]

>>> list(flatten(iterable, levels=3, dictionaries='values'))
[1, 2, 3, 4, 5, 6, 7, 10, (20, {'a1': 30}), 40, 50, 8, 9]

>>> list(flatten(iterable, levels=4, dictionaries='values'))
[1, 2, 3, 4, 5, 6, 7, 10, 20, {'a1': 30}, 40, 50, 8, 9]

>>> list(flatten(iterable, levels=5, dictionaries='values'))
[1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 8, 9]
