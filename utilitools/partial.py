import functools
import itertools


class partial(functools.partial):
    """
    | Creates an object with a simplified signature
      by “freezing” some portion of a function’s arguments and keywords.
    """
    def __new__(cls, function, /, *args, **kwargs):
        """
        | The object inherits from |functools.partial|.

        :param function:
            | Callable to which the partial object will be applied.
        :type function: `callable[any]`
        :param args:
            | Variadic positional arguments will be passed directly
              to the function during initialization.
        :type args: `any`
        :param kwargs:
            | Variadic keywords arguments will be passed directly
              to the function during initialization.
        :type kwargs: `any`
        :return: A partial object with a simplified signature.
        :rtype: :obj:`functools.partial`
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
        :type args: `any`
        :param kwargs:
            | Variadic keywords arguments will be passed directly
              to the function after initialization.
        :type kwargs: `any`
        :return: A partial object with a simplified signature.
        :rtype: :obj:`utilitools.partial`
        :raises BaseException:
            - If `args` does not match to function.
            - If `kwargs` does not match to function.
        """
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        positionals = tuple(filter(lambda arg: arg is not ..., positionals + tuple(iterator)))
        keywords = dict(**self.keywords, **kwargs)
        return self.func(*positionals, **keywords)
