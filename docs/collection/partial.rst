partial
=======

An improved version of `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_ which accepts ``Ellipsis (...)`` as a placeholder.

Usefulness
----------

In Python, there are four types of parameters in function signature:

- Positional (arguments that can be called by their position in the function call)
- Keyword (arguments that can be called by their name)
- Required (arguments that must passed to the function)
- Optional (arguments that can be not passed to the function)

.. note::
   ``*args`` is a positional argument, and ``**kwargs`` is a keyword argument. They are both optional arguments.

We will focus on positional and keyword arguments only. An example of a function for both:

.. code-block:: python

    def func(a, /, b, *, c):
        print(a, b, c)

The types of parameters of the function are:

- ``a`` is positional-only argument
- ``b`` is positional or keyword argument
- ``c`` is keyword-only argument

The limitation of ``functools.partial`` exists with positional-only arguments, which many of Python's built-in functions use.

To illustrate the problem, we will take two built-in functions in Python:

- ``pow`` - `pow(base, exp[, mod]) <https://docs.python.org/3/library/functions.html#int>`_
- ``isinstance`` - `isinstance(object, classinfo) <https://docs.python.org/3/library/functions.html#isinstance>`_

.. note::
   Python's documentation will show ``isinstance(object, classinfo)`` but in fact it is ``ininstance(obj, class_or_tuple, /)``, this can be checked via `inspect.signature <https://docs.python.org/3/library/inspect.html#inspect.signature>`_

Using ``pow(base, exp, mod=None)`` by ``functools.partial`` works perfectly:

- 3\ :sup:`n`: ``functools.partial(pow, 3)``
- n\ :sup:`3`: ``functools.partial(pow, exp=3)``

Using ``isinstance(obj, class_or_tuple, /)`` by ``functools.partial`` are limited:

- isint(obj): ``functools.partial(isinstance, class_or_tuple=int)``

.. warning::
    ``obj`` and ``class_or_tuple`` are positional-only arguments, Therefore we will get an exception: ``TypeError: isinstance() takes no keyword arguments``

``utilitools.partial`` works the same as ``functools.partial``, with the ability to skip any arguments

Another solution for ``pow(base, exp, mod=None)`` by ``utilitools.partial``:

- n\ :sup:`3`: ``utilitools.partial(pow, ..., 3)``

Working solution for ``isinstance(obj, class_or_tuple, /)`` by ``utilitools.partial``:

- isint(obj): ``utilitools.partial(isinstance, ..., int)``

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
