import itertools
import unittest
import utilitools


@utilitools.subscription(tuple)
def function(n):
    return n


@utilitools.subscription(list)
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
        start, stop, step = 10, 25, 3
        actual = function[:stop]
        expected = tuple(range(stop))
        self.assertEqual(expected, actual)
        actual = function[start:stop]
        expected = tuple(range(start, stop))
        self.assertEqual(expected, actual)
        actual = function[start:stop:step]
        expected = tuple(range(start, stop, step))
        self.assertEqual(expected, actual)
        actual = function[stop:start:-step]
        expected = tuple(range(stop, start, -step))
        self.assertEqual(expected, actual)

    def test_generator_by_index(self):
        index = 75
        actual = generator[index]
        expected = index
        self.assertEqual(expected, actual)

    def test_generator_by_slice(self):
        start, stop, step = 10, 25, 3
        actual = generator[:stop]
        expected = list(range(stop))
        self.assertEqual(expected, actual)
        actual = generator[start:stop]
        expected = list(range(start, stop))
        self.assertEqual(expected, actual)
        actual = generator[start:stop:step]
        expected = list(range(start, stop, step))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
