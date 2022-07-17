islice
======

.. autofunction:: utilitools.islice

.. |itertools.islice| raw:: html

   <a href="https://docs.python.org/3/library/itertools.html#itertools.islice" target="_blank">itertools.islice</a>

Examples
--------

.. code-block:: python

    from itertools import count
    from utilitools import islice

Slicing a finite sequence when `start` is negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, -15, None, 3)
>>> list(iterator)
[35, 38, 41, 44, 47]

Slicing a finite sequence when `start` and `stop` are negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, -30, -20, 3)
>>> list(iterator)
[20, 23, 26, 29]

Slicing a finite sequence when `start` and `step` are negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, -30, None, -3)
>>> list(iterator)
[20, 17, 14, 11, 8, 5, 2]

Slicing a finite sequence when `start`, `stop` and `step` are negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, -20, -30, -3)
>>> list(iterator)
[30, 27, 24, 21]

Slicing a finite sequence when `stop` is negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, None, -30, 3)
>>> list(iterator)
[0, 3, 6, 9, 12, 15, 18]

Slicing a finite sequence when `stop` and `step` are negative:

>>> iterable = range(50)
>>> iterator = islice(iterable, None, -20, -3)
>>> list(iterator)
[49, 46, 43, 40, 37, 34, 31]

Slicing an infinite sequence when `step` is negative:

>>> iterable = count()
>>> iterator = islice(iterable, 30, 20, -3)
>>> list(iterator)
[30, 27, 24, 21]
