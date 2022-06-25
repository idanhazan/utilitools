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
        actual = function[index]
        expected = index
        self.assertEqual(expected, actual)
        actual = function[-index]
        expected = -index
        self.assertEqual(expected, actual)

    def test_function_by_slice(self):
        start, stop, end = 10, 25, 3
        actual = function[:stop]
        expected = tuple(range(stop))
        self.assertEqual(expected, actual)
        actual = function[start:stop]
        expected = tuple(range(start, stop))
        self.assertEqual(expected, actual)
        actual = function[start:stop:end]
        expected = tuple(range(start, stop, end))
        self.assertEqual(expected, actual)
        actual = function[stop:start:-end]
        expected = tuple(range(stop, start, -end))
        self.assertEqual(expected, actual)

    def test_generator_by_index(self):
        index = 75
        actual = generator[index]
        expected = index
        self.assertEqual(expected, actual)

    def test_generator_by_slice(self):
        start, stop, end = 10, 25, 3
        actual = generator[:stop]
        expected = list(range(stop))
        self.assertEqual(expected, actual)
        actual = generator[start:stop]
        expected = list(range(start, stop))
        self.assertEqual(expected, actual)
        actual = generator[start:stop:end]
        expected = list(range(start, stop, end))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
