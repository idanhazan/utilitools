import itertools
import unittest
import utilitools


@utilitools.subscriptable(tuple)
def function(n):
    return n


@utilitools.subscriptable(list)
def generator():
    yield from itertools.count()


class Test(unittest.TestCase):
    def test_function_by_index(self):
        index = 75
        self.assertEqual(function[index], index)

    def test_function_by_slice(self):
        start, stop, end = 10, 25, 3
        self.assertEqual(function[:stop], tuple(range(stop)))
        self.assertEqual(function[start:stop], tuple(range(start, stop)))
        self.assertEqual(function[start:stop:end], tuple(range(start, stop, end)))

    def test_generator_by_index(self):
        index = 75
        self.assertEqual(generator[index], index)

    def test_generator_by_slice(self):
        start, stop, end = 10, 25, 3
        self.assertEqual(generator[:stop], list(range(stop)))
        self.assertEqual(generator[start:stop], list(range(start, stop)))
        self.assertEqual(generator[start:stop:end], list(range(start, stop, end)))


if __name__ == '__main__':
    unittest.main()
