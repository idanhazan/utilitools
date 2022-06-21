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

Getting a single value can be done using an index and getting multiple values can be done using a slice:

- ``function[index]`` equals to ``function(index)``.
- ``generator[index]`` equals to ``next(itertools.islice(generator(), index, index + 1))``.
- ``function[start:stop:step]`` equals to ``list(function(n) for n in range(start, stop, step))``.
- ``generator[start:stop:step]`` equals to ``list(itertools.islice(generator(), start, stop, step))``.

.. warning::
    Be aware, both ``function`` and ``generator``
    are already implements ``__call__`` but not ``__getitem__``,
    so without using ``subscriptable`` you will get an exception:
    ``TypeError: 'function' object is not subscriptable``

As you can see, using ``[...]`` is more readable and elegant.

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
