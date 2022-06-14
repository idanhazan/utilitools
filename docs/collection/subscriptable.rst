subscriptable
=============

Subscriptable (in Python) means that an object implements ``__getitem__(self, key)`` magic method.

Usefulness
----------

Assume that there are 2 types of sequences:

- Recursive sequence (called **rs**)
- Non-recursive sequence (called **nrs**)

The sequences look like this:

.. code-block:: python

    import itertools

    def rs():
        yield from itertools.count()

    def nrs(n):
        return n

If we want to get the 25th value:

- rs: ``next(itertools.islice(rs(), 25, 26))``
- nrs: ``nrs(25)``

If we want to get the values between 10 and 20 in steps of 3:

- rs: ``list(itertools.islice(rs(), 10, 20, 3))``
- nrs: ``list(i for i in range(10, 20, 3))``

This task can be elegantly written as follows:

- rs: ``rs[25]`` or ``rs[10:20:3]``
- nrs: ``nrs[25]`` or ``nrs[10:20:3]``

When trying to use elegant writing, we get an exception:

``TypeError: 'function' object is not subscriptable``

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
