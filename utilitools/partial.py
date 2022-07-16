import functools
import itertools


class partial(functools.partial):
    """
    | Creating an object with a simplified signature by “freezing” some portion of a function’s arguments and keywords.

    | An extension of |functools.partial| that accept `Ellipsis` as a placeholder for positional arguments.
    """
    def __call__(self, *args, **kwargs):
        """
        | Apply a partial function.

        :param args:
            | Arguments will be passed to the original function.
        :type args: `any`
        :param kwargs:
            | Keywords rguments will be passed to the original function.
        :type kwargs: `any`
        :return: A partial object with a simplified signature.
        :rtype: :obj:`functools.partial`
        """
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        positionals = tuple(filter(lambda arg: arg is not ..., positionals + tuple(iterator)))
        keywords = dict(**self.keywords, **kwargs)
        return self.func(*positionals, **keywords)
