import functools
import inspect
import itertools


class Partial(functools.partial):
    def __call__(self, *args, **kwargs):
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        keywords = dict(**self.keywords, **kwargs)
        for index, parameter in enumerate(inspect.signature(self.func).parameters.values()):
            is_ellipsis = index < len(positionals) and positionals[index] is ...
            if is_ellipsis and parameter.kind == parameter.POSITIONAL_OR_KEYWORD:
                value = keywords.pop(parameter.name, ...)
                positionals = positionals[:index] + (value,) + positionals[index + 1:]
        positionals = tuple(parameter for parameter in positionals if parameter is not ...)
        return self.func(*positionals, **keywords)
