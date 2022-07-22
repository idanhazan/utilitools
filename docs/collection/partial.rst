partial
=======

.. autoclass:: utilitools.partial

    .. automethod:: __new__

    .. automethod:: __call__

.. |functools.partial| raw:: html

   <a href="https://docs.python.org/3/library/functools.html#functools.partial" target="_blank">functools.partial</a>

Examples
--------

.. code-block:: python

    from utilitools import partial

    def variadic_positional(*args):
        return args

    def positional_only(a, b, c, d=4, e=5, f=6, /):
        return a, b, c, d, e, f

    def positional_or_keyword(a, b, c, d=4, e=5, f=6):
        return a, b, c, d, e, f


Partial function with variadic positional arguments:

>>> partial_func = partial(variadic_positional, ..., ..., 3, 4)
>>> partial_func(1, 2, 5, 6)
(1, 2, 3, 4, 5, 6)

Partial function with positional-only arguments:

>>> partial_func = partial(positional_only, ..., ..., 3, 4)
>>> partial_func(1, 2, 5)
(1, 2, 3, 4, 5, 6)

Partial function with positional or keyword arguments:

>>> partial_func = partial(positional_or_keyword, ..., 2, ..., ..., 5)
>>> partial_func(1, 3, 4)
(1, 2, 3, 4, 5, 6)

>>> partial_func = partial(positional_or_keyword, ..., 2, ..., e=5)
>>> partial_func(1, 3, d=4)
(1, 2, 3, 4, 5, 6)
