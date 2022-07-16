islice
======

.. autofunction:: utilitools.islice

.. |itertools.islice| raw:: html

   <a href="https://docs.python.org/3/library/itertools.html#itertools.islice" target="_blank">itertools.islice</a>

Examples
--------

.. code-block:: python

    from utilitools import islice

    iterable = range(50)

test

>>> iterator = islice(iterable, 20, 30, 3)
>>> list(iterator)
[20, 23, 26, 29]

>>> iterator = islice(iterable, 30, 20, -3)
>>> list(iterator)
[30, 27, 24, 21]

>>> iterator = islice(iterable, 15, -15, 3)
>>> list(iterator)
[15, 18, 21, 24, 27, 30, 33]

>>> iterator = islice(iterable, -15, 15, -3)
>>> list(iterator)
[35, 32, 29, 26, 23, 20, 17]

>>> iterator = islice(iterable, -30, -20, 3)
>>> list(iterator)
[20, 23, 26, 29]

>>> iterator = islice(iterable, -20, -30, -3)
>>> list(iterator)
[30, 27, 24, 21]
