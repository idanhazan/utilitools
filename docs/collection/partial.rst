partial
=======

An improved version of `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_ which accepts ``Ellipsis (...)`` as a placeholder.

Usefulness
----------

In Python, there are two types of parameters in function signature:

- Positional (arguments that can be called by their position)
- Keyword (arguments that can be called by their name)

.. code-block:: python

    def func(a, b, /, c, d, *, e, f):
        print(a, b, c, d, e, f)

.. note::
    Parameters before ``/`` are positional-only.

    Parameters between ``/`` to ``*`` are positional-or-keyword.

    Parameters after ``*`` are keyword-only.

Each parameter has two attributes:

- Required (arguments that must passed to the function)
- Optional (arguments that can be not passed to the function)

.. note::
    ``*args`` are positional-only (optional).

    ``**kwargs`` are keyword-only (optional).

The limitation of ``functools.partial`` exists with positional-only arguments, which many of Python's built-in functions use.

To illustrate the problem, we will take two built-in functions in Python:

- The built-in function: `pow(base, exp[, mod]) <https://docs.python.org/3/library/functions.html#int>`_
- The built-in function: `isinstance(object, classinfo) <https://docs.python.org/3/library/functions.html#isinstance>`_

.. note::
    Python's documentation will show ``isinstance(object, classinfo)`` but in fact it is ``ininstance(obj, class_or_tuple, /)``,
    this can be checked via `inspect.signature <https://docs.python.org/3/library/inspect.html#inspect.signature>`_

Using ``functools.partial``:

- Function of 3\ :sup:`n`: ``functools.partial(pow, 3)``
- Function of n\ :sup:`3`: ``functools.partial(pow, exp=3)``
- Function of is_int(obj): ``functools.partial(isinstance, class_or_tuple=int)``

.. warning::
    ``obj`` and ``class_or_tuple`` are positional-only arguments, Therefore we will get an exception: ``TypeError: isinstance() takes no keyword arguments``.

Using ``utilitools.partial``:

- Function of 3\ :sup:`n`: ``utilitools.partial(pow, 3)``
- Function of n\ :sup:`3`: ``utilitools.partial(pow, exp=3)``
- Function of n\ :sup:`3`: ``utilitools.partial(pow, ..., 3)``
- Function of is_int(obj): ``utilitools.partial(isinstance, ..., int)``

Each ``Ellipsis (...)`` will skip an argument depending on the desired order.

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
