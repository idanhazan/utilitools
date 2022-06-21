subscriptable
=============

Subscriptable (in Python) means that an object implements the ``__getitem__(self, key)`` magic method.

Usefulness
----------

Let's talk about two kinds of magic methods in Python:

- To use ``(...)``, needed implement ``__call__(self, *args, **kwargs)``.
- To use ``[...]``, needed implement ``__getitem__(self, key)``.

A piece of code of an infinite sequence implemented by function and generator:

.. code-block:: python

    import itertools

    def function(n):
        return n

    def generator():
        yield from itertools.count()

Defining abbreviations:

- ``function`` will be called ``f``.
- ``generator`` will be called ``g``.

Getting a single value can be done using an index and getting multiple values can be done using a slice:

- ``f[index]`` equals to ``f(index)``.
- ``g[index]`` equals to ``next(itertools.islice(g(), index, index + 1))``.
- ``f[start:stop:step]`` equals to ``list(f(n) for n in range(start, stop, step))``.
- ``g[start:stop:step]`` equals to ``list(itertools.islice(g(), start, stop, step))``.

.. warning::
    Both ``f`` and ``g`` by default are already implements ``__call__``, but not ``__getitem__``, that's means you will get an exception: ``TypeError: 'function' object is not subscriptable``.

As seen, using ``[...]`` is more readable and elegant than ``(...)``.

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
