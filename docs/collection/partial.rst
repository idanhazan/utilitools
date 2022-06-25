partial
=======

An improved version of `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_ which accepts ``Ellipsis (...)`` as a placeholder.

Background
----------

In Python, there are two kinds of parameters in function signature:

- Positional (arguments that can be called by their position)
- Keyword (arguments that can be called by their name)

A piece of code that will show all the parameter kinds:

.. code-block:: python

    from inspect import signature

    def describe(func):
        for parameter in signature(func).parameters.values():
            yield f'Parameter {parameter.name!r} is {parameter.kind.description}.'

    if __name__ == '__main__':
        print(*describe(lambda a, b, /, c, d, *, e, f: ...), sep='\n')
        # Parameter 'a' is positional-only.
        # Parameter 'b' is positional-only.
        # Parameter 'c' is positional or keyword.
        # Parameter 'd' is positional or keyword.
        # Parameter 'e' is keyword-only.
        # Parameter 'f' is keyword-only.

        print(*describe(lambda *args, **kwargs: ...), sep='\n')
        # Parameter 'args' is variadic positional.
        # Parameter 'kwargs' is variadic keyword.

For more information: `inspect.Parameter.kind <https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind>`_

The limitation of ``functools.partial`` exists with positional-only arguments,
which many of Python's built-in functions use.

Let's take the built-in function: `isinstance <https://docs.python.org/3/library/functions.html#isinstance>`_

.. note::
    In Python documentation,
    the function signature is ``isinstance(object, classinfo)``,
    but the actual function signature is ``ininstance(obj, class_or_tuple, /)``

Creating a partial function that checks if an object instance is an integer:

.. code-block:: python

    from utilitools import partial

    if __name__ == '__main__':
        is_integer = partial(isinstance, ..., int)
        print(is_integer(25))   # True
        print(is_integer('25')) # False

Each placeholder allows passing a single argument (including kind of positional-only arguments).

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
        func1 = partial(func, ..., 2,   3, ..., f=6) # 'c' passed as a positional argument
        func2 = partial(func, ..., 2, c=3, ..., f=6) # 'c' passed as a keyword argument

        # Because of 'c' passed as a positional argument, 'd' can be given as a positional or keyword argument
        result1 = func1(1,   4, e=5) # 'd' passed as a positional argument
        result2 = func1(1, d=4, e=5) # 'd' passed as a keyword argument

        # Because of 'c' passed as a keyword argument, 'd' can be given as a keyword-only argument
        result3 = func2(1, d=4, e=5) # 'd' passed as keyword argument

        print(result1) # 1, 2, 3, 4, 5, 6
        print(result2) # 1, 2, 3, 4, 5, 6
        print(result3) # 1, 2, 3, 4, 5, 6