singleton
=========

.. autoclass:: utilitools.singleton

    .. automethod:: __call__

Examples
--------

.. code-block:: python

    import logging
    import pathlib
    import sys

    from utilitools import singleton

    class Logger(metaclass=singleton):
        def __init__(self, name, level, stream_handler, file_handler):
            self._logger = logging.getLogger(name)
            self._logger.setLevel(level)
            self._logger.addHandler(stream_handler)
            self._logger.addHandler(file_handler)

        def log(self, level, msg, *args, **kwargs):
            self._logger.log(level, msg, *args, **kwargs)

Create a logger singleton instance:

>>> Logger(
...     name=__name__,
...     level=logging.DEBUG,
...     stream_handler=logging.StreamHandler(sys.stdout),
...     file_handler=logging.FileHandler(pathlib.Path().resolve().joinpath('singleton.log')),
... )

Get the logger instance from anywhere:

>>> logger = Logger()
>>> logger.log(logging.DEBUG, 'A logging message.')
