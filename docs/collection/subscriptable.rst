subscriptable
=============

Subscriptable (in Python) means that an object implements the ``__getitem__(self, key)`` magic method.

Background
----------

Let's talk about two kinds of magic methods in Python:

- To use ``object(...)``, needed implement ``__call__(self, *args, **kwargs)``.
- To use ``object[...]``, needed implement ``__getitem__(self, key)``.

A piece of code of an infinite sequence implemented by function and generator:

.. code-block:: python

    import itertools

    def function(n):
        return n

    def generator():
        yield from itertools.count()

Both ``function`` and ``generator`` are functions acts as sequences,
thus using ``func[...]`` is more readable and elegant than ``func(...)``.

An example of ``__getitem__`` magic method:

- ``function[index]``
- ``generator[index]``
- ``function[start:stop:step]``
- ``generator[start:stop:step]``

.. warning::
    Be aware ``__getitem__`` not implemented by default on functions,
    using ``func[...]`` will raise an exception
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
