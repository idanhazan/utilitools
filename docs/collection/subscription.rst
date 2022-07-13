subscription
============

A subscription object (in Python) means it implements the ``__getitem__(self, key)`` magic method.

.. autofunction:: utilitools.subscription

Background
----------

Subscription is a private case of function use (valid for a situation where the function behaves like a sequence).
When needed, it makes the code more readable and, of course, “pythonic” syntax.

.. code-block:: python

    def func(x):
        return x

>>> func[index]
TypeError: 'function' object is not subscriptable

>>> func[start:stop:step]
TypeError: 'function' object is not subscriptable

Usage
-----

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

>>> digital_sum[123]
6

>>> digital_sum[10:20:3]
(1, 4, 7, 10)

>>> fibonacci[123]
22698374052006863956975682

>>> fibonacci[10:20:3]
[55, 233, 987, 4181]
