subscription
============

.. autofunction:: utilitools.subscription

Examples
--------

.. code-block:: python

    from utilitools import subscription

    @subscription(tuple)
    def digital_sum(n):
        return sum(map(int, str(n)))

    @subscription(list)
    def fibonacci():
        a, b = 0, 1
        yield a
        while True:
            a, b = b, a + b
            yield a

Subscription (func_type: `function` | iter_type: `tuple` | key: `int`)

>>> digital_sum[123]
6

Subscription (func_type: `function` | iter_type: `tuple` | key: `slice`)

>>> digital_sum[10:20:3]
(1, 4, 7, 10)

Subscription (func_type: `generator` | iter_type: `list` | key: `int`)

>>> fibonacci[123]
22698374052006863956975682

Subscription (func_type: `generator` | iter_type: `list` | key: `slice`)

>>> fibonacci[10:20:3]
[55, 233, 987, 4181]
