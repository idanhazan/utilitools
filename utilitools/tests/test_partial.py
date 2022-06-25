import unittest
import utilitools


def variadic_positional(*args):
    return args


def variadic_keyword(**kwargs):
    return kwargs


def positional_only(a, b, c, d=4, e=5, f=6, /):
    return a, b, c, d, e, f


def positional_or_keyword(a, b, c, d=4, e=5, f=6):
    return a, b, c, d, e, f


def keyword_only(*, a, b, c, d=4, e=5, f=6):
    return a, b, c, d, e, f


class Test(unittest.TestCase):
    def test_variadic_positional(self):
        partial = utilitools.partial(variadic_positional, ..., ..., 3, 4)
        actual = partial(1, 2, 5, 6)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(expected, actual)

    def test_variadic_keyword(self):
        partial = utilitools.partial(variadic_keyword)
        actual = partial(a=1, b=2, c=3, d=4, e=5, f=6)
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        self.assertEqual(expected, actual)

    def test_positional_only(self):
        partial = utilitools.partial(positional_only, ..., ..., 3, 4)
        actual = partial(1, 2, 5, 6)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(expected, actual)

    def test_positional_or_keyword(self):
        partial = utilitools.partial(positional_or_keyword, ..., 2, ..., ..., 5, f=6)
        actual = partial(1, 3, 4)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(expected, actual)
        partial = utilitools.partial(positional_or_keyword, ..., 2, ..., e=5, f=6)
        actual = partial(1, 3, d=4)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(expected, actual)

    def test_keyword_only(self):
        partial = utilitools.partial(keyword_only, b=2, d=4, f=6)
        actual = partial(a=1, c=3, e=5)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
