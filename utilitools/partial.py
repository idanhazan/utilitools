import functools


class Partial(functools.partial):
    def __call__(self, *args, **kwargs):
        iterator = iter(args)
        arguments = (next(iterator) if arg is ... else arg for arg in self.args)
        keywords = {**self.keywords, **kwargs}
        return self.func(*arguments, *iterator, **keywords)
