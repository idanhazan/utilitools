partial
=======

An improved version of ``functools.partial`` which accepts ``Ellipsis (...)`` as a placeholder.

Usefulness
----------

In Python there is 2 types of arguments in function signature:

- Positional arguments
- Keyword arguments

Look at this function signature:

.. code-block:: python

    def func(a, /, b, *, c):
        print(a, b, c)

There are 3 arguments:

- ``a`` is ``Positional only``
- ``b`` is ``Positional & Keyword``
- ``c`` is ``Keyword only``

For ``(a=1, b=2, c=3)`` we can call that function by:

- ``func(1, 2, c=3)``
- ``func(1, b=2, c=3)``
- ``func(1, c=3, b=2)``

As you can see, ``a`` cannot specify as ``a=1`` and ``c`` must specify as ``c=3``

The limitation of ``itertools.partial`` exists on ``Positional only`` arguments, and most of Python's built-in functions use it.

Let's say we want to check if an iterable contains only integers:

- Step 1: ``isinstance(object, classinfo, /)``
- Step 2: ``functools.partial(func, /, *args, **keywords)``
- Step 3: ``map(function, iterable, ..., /)``
- Step 4: ``all(iterable, /)``

Using ``functools.partial`` is impossible:

- ``all(map(functools.partial(isinstance, int), [1, 2, 3]))`` translated as ``isinstance(classinfo, object, /)``
- ``all(map(functools.partial(isinstance, classinfo=int), [1, 2, 3]))`` not allowed because of ``/``

Using ``utilitools.partial`` will solve this problem:

- ``all(map(utilitools.partial(isinstance, ..., int), [1, 2, 3]))``

Source
------

https://github.com/idanhazan/utilitools/blob/main/utilitools/partial.py

Usage
-----

.. code-block:: python

   from utilitools import partial

   if __name__ == '__main__':
       all(map(partial(isinstance, ..., int), [1, 2, 3])  # True
       any(map(partial(isinstance, ..., str), [1, 2, 3])  # False
