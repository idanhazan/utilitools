singleton
=========

Singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.

Usefulness
----------

Logging is a specific example of an "acceptable" Singleton because it doesn't affect the execution of the code.


Source
------

https://github.com/idanhazan/utilitools/blob/main/utilitools/singleton.py

Usage
-----

.. code-block:: python

   from utilitools import singleton

   class Singleton(metaclass=singleton):
       def __init__(self, *args, **kwargs):
           self.args = args
           self.kwargs = kwargs

       def __repr__(self):
           return f'{self.__class__.__name__}(args={self.args}, kwargs={self.kwargs})'

   if __name__ == '__main__':
       Singleton(1, 2, x=10, y=20)  # Singleton(args=(1, 2), kwargs={'x': 10, 'y': 20})
       Singleton().args             # (1, 2)
       Singleton().kwargs           # {'x': 10, 'y': 20}
