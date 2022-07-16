partial
=======

.. autoclass:: utilitools.partial

    .. automethod:: __call__

.. |functools.partial| raw:: html

   <a href="https://docs.python.org/3/library/functools.html#functools.partial" target="_blank">functools.partial</a>

Examples
--------

.. code-block:: python

    from utilitools import partial

    def func(a, b, c, /, d, e, f, g, h, *, i, j):
        return a, b, c, d, e, f, g, h, i, j

>>> partial_func = partial(func, ..., 1, ..., ..., 4, h=7, j=9)
>>> partial_func(0, 2, 3, 5, g=6, i=8)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
