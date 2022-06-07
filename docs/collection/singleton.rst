singleton
=========

Singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance.

Usage
-----

.. code-block:: python
   :caption: singleton.py

   from utilitools import Singleton

   class SharedResource(metaclass=Singleton):
       def __init__(self, *args, **kwargs):
           self.args = args
           self.kwargs = kwargs

   def __repr__(self):
       return f'{self.__class__.__name__}(args={self.args}, kwargs={self.kwargs})'

   if __name__ == '__main__':
       SharedResource(1, 2, x=10, y=20)  # SharedResource(args=(1, 2), kwargs={'x': 10, 'y': 20})
       SharedResource().args             # (1, 2)
       SharedResource().kwargs           # {'x': 10, 'y': 20}
