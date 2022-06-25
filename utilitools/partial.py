import functools
import itertools


class Partial(functools.partial):
    def __call__(self, *args, **kwargs):
        iterator = iter(args + tuple(itertools.repeat(..., self.args.count(...) - len(args))))
        positionals = tuple(next(iterator) if arg is ... else arg for arg in self.args)
        positionals = tuple(filter(lambda arg: arg is not ..., positionals + tuple(iterator)))
        keywords = dict(**self.keywords, **kwargs)
        return self.func(*positionals, **keywords)
