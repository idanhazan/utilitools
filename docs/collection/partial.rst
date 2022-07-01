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
    Information about the types of parameters can be found in the documentation of
    `inspect.Parameter.kind <https://docs.python.org/3/library/inspect.html#inspect.Parameter.kind>`_.

.. code-block:: python

    def div(numerator, denominator, /):
        return numerator / denominator

>>> div_6_n = functools.partial(div, 6)
>>> div_6_n(2)
3.0

>>> div_n_2 = functools.partial(div, denominator=2)
>>> div_n_2(6)
TypeError: div() got some positional-only arguments passed as keyword arguments: 'denominator'

Usage
-----

.. code-block:: python

    from utilitools import partial

    def func(a, b, /, c, d, *, e, f):
        return a, b, c, d, e, f

    func1 = partial(func, ..., 2,   3, ..., f=6)
    func2 = partial(func, ..., 2, c=3, ..., f=6)

    # func1 is similar to func(..., 2, /,   3,   ..., *, e=..., f=6)
    # func2 is similar to func(..., 2, /, c=3, d=..., *, e=..., f=6)

>>> func1(1, 4, e=5)
(1, 2, 3, 4, 5, 6)

>>> func1(1, d=4, e=5)
(1, 2, 3, 4, 5, 6)

>>> func2(1, d=4, e=5)
(1, 2, 3, 4, 5, 6)
