subscriptable
=============

Subscriptable (in Python) means that an object implements the ``__getitem__(self, key)`` magic method.

Usefulness
----------

There are two types of sequences:

- Recursive sequence (acronyms for **rs**)
- Non-recursive sequence (acronyms for **nrs**)

The sequences look like this:

.. code-block:: python

    import itertools

    def rs():
        yield from itertools.count()

    def nrs(n):
        return n

To get a specific value or list of values from the sequences, we can use this table:

.. list-table::
   :widths: 10 10 40 40
   :header-rows: 1

   * - Sequence
     - Bracket
     - Index
     - Slice
   * - rs
     - (...)
     - ``next(islice(rs(), 25, 26))``
     - ``list(islice(rs(), 10, 20, 3))``
   * - nrs
     - (...)
     - ``nrs(25)``
     - ``list(nrs(n) for n in range(10, 20, 3))``
   * - rs
     - [...]
     - ``rs[25]``
     - ``rs[10:20:3]``
   * - nrs
     - [...]
     - ``nrs[25]``
     - ``nrs[10:20:3]``

.. note::
   The ``islice`` function is part of the `itertools <https://docs.python.org/3/library/itertools.html#itertools.islice>`_ package.

When trying to use ``[...]`` brackets, we get an exception:

``TypeError: 'function' object is not subscriptable``

In this package, subscriptable is a decorator that allows using ``[...]`` brackets on functions.

Source
------

https://github.com/idanhazan/utilitools/blob/main/utilitools/subscriptable.py

Usage
-----

.. code-block:: python

   from utilitools import subscriptable

   @subscriptable(tuple)
   def digitsum(n):
      return sum(map(int, str(n)))

   @subscriptable(list)
   def fibonacci():
       a, b = 0, 1
       yield a
       while True:
           a, b = b, a + b
           yield a

   if __name__ == '__main__':
       digitsum[123]       # 6
       digitsum[10:20:3]   # (1, 4, 7, 10)
       fibonacci[123]      # 22698374052006863956975682
       fibonacci[10:20:3]  # [55, 233, 987, 4181]
