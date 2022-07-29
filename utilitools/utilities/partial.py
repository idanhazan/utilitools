import functools
import itertools


class partial(functools.partial):
    """
    | An extended version (handling positional arguments)
      that inherits from |functools.partial|.
    """
    def __new__(cls, function, /, *args, **kwargs):
        """
        | Creates an object with
          a simplified signature by “freezing” some portion of
          a function’s positional and keyword arguments.

        :param function:
            | Callable to which the partial object will be applied.
        :type function: collections.Callable

        :param args:
            | Variadic positional arguments will be passed directly
              to the function during initialization.
        :type args: typing.Any

        :param kwargs:
            | Variadic keywords arguments will be passed directly
              to the function during initialization.
        :type kwargs: typing.Any

        :return: A partial object with a simplified signature.
        :rtype: :obj:`utilitools.partial`

        :raises TypeError:
            - If `function` is not callable.
        """
        return super(partial, cls).__new__(cls, function, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        | An extension that accepts `Ellipsis`
          as a placeholder for positional arguments.

        :param args:
            | Variadic positional arguments will be passed directly
              to the function after initialization.
        :type args: typing.Any

        :param kwargs:
            | Variadic keywords arguments will be passed directly
              to the function after initialization.
        :type kwargs: typing.Any

        :return: The output of the function.
        :rtype: typing.Any

        :raises BaseException:
            - If `args` does not match to function.
            - If `kwargs` does not match to function.
        """
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        positionals = tuple(filter(lambda arg: arg is not ..., positionals + tuple(iterator)))
        keywords = dict(**self.keywords, **kwargs)
        return self.func(*positionals, **keywords)
