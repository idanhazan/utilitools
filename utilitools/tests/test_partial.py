import unittest
import utilitools


class Test(unittest.TestCase):
    def test_variadic_function(self):
        func = utilitools.partial(lambda *args, **kwargs: (args, kwargs), ..., 2, ..., d=4)
        positionals, keywords = (1, 2, 3), {'d': 4, 'e': 5}
        self.assertEqual(func(1, 3, e=5), (positionals, keywords))
        positionals, keywords = (1, 2), {'d': 4, 'c': 3, 'e': 5}
        self.assertEqual(func(1, c=3, e=5), (positionals, keywords))

    def test_positional_only(self):
        func = utilitools.partial(lambda a, b, c, /: (a, b, c), ..., 2, ...)
        self.assertEqual(func(1, 3), (1, 2, 3))

    def test_positional_or_keyword(self):
        func = utilitools.partial(lambda a, b, /, c, d, *, e, f: (a, b, c, d, e, f), ..., 2, ..., 4, f=6)
        self.assertEqual(func(1, 3, e=5), (1, 2, 3, 4, 5, 6))
        self.assertEqual(func(1, c=3, e=5), (1, 2, 3, 4, 5, 6))
        func = utilitools.partial(lambda a, b, /, c, d, *, e, f: (a, b, c, d, e, f), ..., 2, ..., d=4, f=6)
        self.assertEqual(func(1, 3, e=5), (1, 2, 3, 4, 5, 6))
        self.assertEqual(func(1, c=3, e=5), (1, 2, 3, 4, 5, 6))

    def test_keyword_only(self):
        func = utilitools.partial(lambda *, a, b, c: (a, b, c), b=2)
        self.assertEqual(func(a=1, c=3), (1, 2, 3))


if __name__ == '__main__':
    unittest.main()
