partial
=======

Partial function application that “freezes” some portion of a function’s arguments and keywords, resulting in a new object with a simplified signature.

.. autoclass:: utilitools.partial

Background
----------

The built-in ``functools`` module contains:

- `functools.partial <https://docs.python.org/3/library/functools.html#functools.partial>`_
- `functools.partialmethod <https://docs.python.org/3/library/functools.html#functools.partialmethod>`_

Both are limited, and as a result, they require positional-only arguments without allowing to skip some.

.. note::
    Python 3.8 has started supporting positional-only arguments and some of built-in functions already use it.
    Information about the types of parameters can be found in the documentation of
    `inspect.Parameter.kind <https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind>`_.

We will use the `divmod <https://docs.python.org/3/library/functions.html#divmod>`_ built-in function:

.. warning::
    The function's signature in the documentation is incorrect.

>>> inspect.signature(divmod)
<Signature (x, y, /)>

It is not possible to use function ``divmod``
and provide a value for parameter ``y`` (i.e. skip parameter ``x``).

Usage
-----

.. code-block:: python

    from utilitools import partial

    def func(a, b, c, /, d, e, f, g, h, *, i, j):
        return a, b, c, d, e, f, g, h, i, j

>>> partial_func = partial(func, ..., 1, ..., ..., 4, h=7, j=9)
>>> partial_func(0, 2, 3, 5, g=6, i=8)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
