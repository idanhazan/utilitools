partial
=======

An improved version of `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_ which accepts ``Ellipsis (...)`` as a placeholder.

Usefulness
----------

In Python, there are two types of arguments in function signature:

- Positional arguments
- Keyword arguments

See an example of both:

.. code-block:: python

    def func(a, /, b, *, c):
        print(a, b, c)

The types of arguments of the function are:

- ``a`` is ``Positional only``
- ``b`` is ``Positional or Keyword``
- ``c`` is ``Keyword only``

To call the function (where ``a=1``, ``b=2``, ``c=3``), there are only three possible options:

- ``func(1, 2, c=3)``
- ``func(1, b=2, c=3)``
- ``func(1, c=3, b=2)``

The limitation of ``functools.partial`` exists with positional only arguments, which many of Python's built-in functions use.

To illustrate the problem, we will take two built-in functions in Python:

- `pow(base, exp, mod=None) <https://docs.python.org/3/library/functions.html#int>`_
- `isinstance(obj, class_or_tuple, /) <https://docs.python.org/3/library/functions.html#isinstance>`_

.. note::
   Python's documentation will show ``isinstance(object, classinfo)`` but in fact it is ``ininstance(obj, class_or_tuple, /)``, this can be checked via `inspect.signature <https://docs.python.org/3/library/inspect.html#inspect.signature>`_ by: ``inspect.signature(isinstance)``

Using ``functools.partial``:

- ``pow(base, exp, mod=None)``
 - To create a function of 3\ :sup:`n`, use: ``functools.partial(pow, 3)``
 - To create a function of n\ :sup:`3`, use: ``functools.partial(pow, exp=3)``
- ``isinstance(obj, class_or_tuple, /)``
 - Creating a function that checks if an instance is an integer is impossible:
  - ``functools.partial(isinstance, class_or_tuple=int)`` raise: ``TypeError: isinstance() takes no keyword arguments``
  - ``functools.partial(isinstance, classinfo=int)`` raise: ``TypeError: isinstance() takes no keyword arguments``

Using ``utilitools.partial``:

- ``pow(base, exp, mod=None)``
 - To create a function of 3\ :sup:`n`, use: ``utilitools.partial(pow, 3)``
 - To create a function of n\ :sup:`3`, use: ``utilitools.partial(pow, exp=3)``
 - To create a function of n\ :sup:`3`, use: ``utilitools.partial(pow, ..., 3)``
- ``isinstance(obj, class_or_tuple, /)``
 - To create a function ``is_int``, use: ``utilitools.partial(isinstance, ..., int)``

Each ``Ellipsis (...)`` will skip an argument even if it is positional only.

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
