singleton
=========

.. autoclass:: utilitools.singleton

    .. automethod:: __call__

Examples
--------

.. code-block:: python

   from utilitools import singleton

   class Singleton(metaclass=singleton):
       def __init__(self, *args, **kwargs):
           self.args = args
           self.kwargs = kwargs

       def __repr__(self):
           return f'{self.__class__.__name__}(args={self.args}, kwargs={self.kwargs})'

>>> Singleton(1, 2, x=10, y=20)
Singleton(args=(1, 2), kwargs={'x': 10, 'y': 20})

>>> Singleton().args
(1, 2)

>>> Singleton().kwargs
{'x': 10, 'y': 20}
