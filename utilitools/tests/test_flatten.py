import unittest
import utilitools


class Test(unittest.TestCase):
    def setUp(self):
        self.iterable = [0, (1, {2, 3}, 4), (5, {6, 7}, 8), 9]

    def tearDown(self):
        del self.iterable

    def test_flatten(self):
        actual = list(utilitools.flatten(self.iterable))
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, actual)

    def test_flatten_with_levels(self):
        pass
        actual = list(utilitools.flatten(self.iterable, levels=0))
        expected = [0, (1, {2, 3}, 4), (5, {6, 7}, 8), 9]
        self.assertEqual(expected, actual)
        actual = list(utilitools.flatten(self.iterable, levels=1))
        expected = [0, 1, {2, 3}, 4, 5, {6, 7}, 8, 9]
        self.assertEqual(expected, actual)
        actual = list(utilitools.flatten(self.iterable, levels=2))
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, actual)

    def test_flatten_with_types(self):
        actual = list(utilitools.flatten(self.iterable, types=(list,)))
        expected = [[0, (1, {2, 3}, 4), (5, {6, 7}, 8), 9]]
        self.assertEqual(expected, actual)
        actual = list(utilitools.flatten(self.iterable, types=(tuple,)))
        expected = [0, (1, {2, 3}, 4), (5, {6, 7}, 8), 9]
        self.assertEqual(expected, actual)
        actual = list(utilitools.flatten(self.iterable, types=(set,)))
        expected = [0, 1, {2, 3}, 4, 5, {6, 7}, 8, 9]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
