partial
=======

An improved version of `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_ which accepts ``Ellipsis (...)`` as a placeholder.

Usefulness
----------

In Python, there are two kinds of parameters in function signature:

- Positional (arguments that can be called by their position)
- Keyword (arguments that can be called by their name)

.. code-block:: python

    import inspect

    def describe(func):
        for parameter in inspect.signature(func).parameters.values():
            print(f'Parameter {parameter.name!r} is {parameter.kind.description}.')

    if __name__ == '__main__':
        f1 = lambda a, b, /, c, d, *, e, f: ...
        f2 = lambda *args, **kwargs: ...

        describe(f1)
        # Parameter 'a' is positional-only.
        # Parameter 'b' is positional-only.
        # Parameter 'c' is positional or keyword.
        # Parameter 'd' is positional or keyword.
        # Parameter 'e' is keyword-only.
        # Parameter 'f' is keyword-only.

        describe(f2)
        # Parameter 'args' is variadic positional.
        # Parameter 'kwargs' is variadic keyword.

The limitation of ``functools.partial`` exists with positional-only arguments, which many of Python's built-in functions use.

To illustrate the problem, we will take two built-in functions in Python:

- The built-in function: `pow(base, exp[, mod]) <https://docs.python.org/3/library/functions.html#pow>`_
- The built-in function: `isinstance(object, classinfo) <https://docs.python.org/3/library/functions.html#isinstance>`_

.. note::
    Python's documentation will show ``isinstance(object, classinfo)`` but in fact it is ``ininstance(obj, class_or_tuple, /)``,
    this can be checked via `inspect.signature <https://docs.python.org/3/library/inspect.html#inspect.signature>`_

Using ``functools.partial``:

- Function of 3\ :sup:`n`: ``functools.partial(pow, 3)``
- Function of 3\ :sup:`n`: ``functools.partial(pow, base=3)``
- Function of n\ :sup:`3`: ``functools.partial(pow, exp=3)``
- Function of is_int(obj): ``functools.partial(isinstance, class_or_tuple=int)``

.. warning::
    ``obj`` and ``class_or_tuple`` are positional-only arguments, Therefore we will get an exception: ``TypeError: isinstance() takes no keyword arguments``.

Using ``utilitools.partial``:

- Function of 3\ :sup:`n`: ``utilitools.partial(pow, 3)``
- Function of 3\ :sup:`n`: ``utilitools.partial(pow, base=3)``
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

    def func(a, b, /, c, d, *, e, f):
        return a, b, c, d, e, f

    if __name__ == '__main__':
        f1 = partial(func, ..., 2, ..., 4, f=6)
        f2 = partial(func, ..., 2, ..., d=4, f=6)

        f1(1, 3, e=5)    # 1, 2, 3, 4, 5, 6
        f1(1, c=3, e=5)  # 1, 2, 3, 4, 5, 6
        f2(1, 3, e=5)    # 1, 2, 3, 4, 5, 6
        f2(1, c=3, e=5)  # 1, 2, 3, 4, 5, 6
