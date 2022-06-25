subscriptable
=============

A subscription object (in Python) means it implements the ``__getitem__(self, key)`` magic method.

.. autofunction:: utilitools.subscriptable

Background
----------

.. code-block:: python

    def func(*args, **kwargs):
        ...

Valid cases of ``__getitem__``:

- func[index]
- func[start:]
- func[start:stop]
- func[start:stop:step]
- func[start::step]
- func[:stop]
- func[:stop:step]

.. warning::
    Be aware ``__getitem__`` not implemented by default on functions,
    thus it will raise an exception
    ``TypeError: 'function' object is not subscriptable``

Usage
-----

.. code-block:: python

    from utilitools import subscriptable

    @subscriptable(tuple)
    def digital_sum(n):
        return sum(map(int, str(n)))

    @subscriptable(list)
    def fibonacci():
        a, b = 0, 1
        yield a
        while True:
            a, b = b, a + b
            yield a

    if __name__ == '__main__':
        print(digital_sum[123])      # 6
        print(digital_sum[10:20:3])  # (1, 4, 7, 10)
        print(fibonacci[123])        # 22698374052006863956975682
        print(fibonacci[10:20:3])    # [55, 233, 987, 4181]
