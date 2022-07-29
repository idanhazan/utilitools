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

        Parameters
        ----------
        function : collections.Callable
            | Callable to which the partial object will be applied.
        args : typing.Any
            | Variadic positional arguments will be passed directly
              to the function during initialization.
        kwargs : typing.Any
            | Variadic keywords arguments will be passed directly
              to the function during initialization.

        Returns
        -------
        utilitools.partial
            | A partial object with a simplified signature.

        Raises
        ------
        TypeError
            - If `function` is not callable.
        """
        return super(partial, cls).__new__(cls, function, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        | An extension that accepts `Ellipsis`
          as a placeholder for positional arguments.

        Parameters
        ----------
        args : typing.Any
            | Variadic positional arguments will be passed directly
              to the function after initialization.
        kwargs : typing.Any
            | Variadic keywords arguments will be passed directly
              to the function after initialization.

        Raises
        ------
        BaseException
            - If `args` does not match to function.
            - If `kwargs` does not match to function.
        """
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        positionals = tuple(filter(lambda arg: arg is not ..., positionals + tuple(iterator)))
        keywords = dict(**self.keywords, **kwargs)
        return self.func(*positionals, **keywords)
