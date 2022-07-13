import itertools
import unittest
import utilitools


class Test(unittest.TestCase):
    def setUp(self):
        self.iterable_a = range(50)
        self.iterable_b = iter(range(50))
        self.iterable_c = itertools.islice(range(50), None)

    def tearDown(self):
        del self.iterable_a
        del self.iterable_b
        del self.iterable_c

    def test_iterables(self):
        actual = hasattr(self.iterable_a, '__len__') or hasattr(self.iterable_a, '__length_hint__')
        expected = True
        self.assertEqual(expected, actual)
        actual = hasattr(self.iterable_b, '__len__') or hasattr(self.iterable_b, '__length_hint__')
        expected = True
        self.assertEqual(expected, actual)
        actual = hasattr(self.iterable_c, '__len__') or hasattr(self.iterable_c, '__length_hint__')
        expected = False
        self.assertEqual(expected, actual)
        actual = hasattr(self.iterable_a, '__reversed__')
        expected = True
        self.assertEqual(expected, actual)
        actual = hasattr(self.iterable_b, '__reversed__')
        expected = False
        self.assertEqual(expected, actual)
        actual = hasattr(self.iterable_c, '__reversed__')
        expected = False
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_a1(self):
        iterable, start, stop, step = self.iterable_a, 20, 30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_a2(self):
        iterable, start, stop, step = self.iterable_a, 25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_a3(self):
        iterable, start, stop, step = self.iterable_a, 30, 20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_b1(self):
        iterable, start, stop, step = self.iterable_b, 20, 30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_b2(self):
        iterable, start, stop, step = self.iterable_b, 25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_b3(self):
        iterable, start, stop, step = self.iterable_b, 30, 20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_c1(self):
        iterable, start, stop, step = self.iterable_c, 20, 30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_c2(self):
        iterable, start, stop, step = self.iterable_c, 25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_positive_c3(self):
        iterable, start, stop, step = self.iterable_c, 30, 20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_a1(self):
        iterable, start, stop, step = self.iterable_a, 20, 30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_a2(self):
        iterable, start, stop, step = self.iterable_a, 25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_a3(self):
        iterable, start, stop, step = self.iterable_a, 30, 20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_b1(self):
        iterable, start, stop, step = self.iterable_b, 20, 30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_b2(self):
        iterable, start, stop, step = self.iterable_b, 25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_b3(self):
        iterable, start, stop, step = self.iterable_b, 30, 20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_c1(self):
        iterable, start, stop, step = self.iterable_c, 20, 30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_c2(self):
        iterable, start, stop, step = self.iterable_c, 25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_positive_negative_c3(self):
        iterable, start, stop, step = self.iterable_c, 30, 20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_a1(self):
        iterable, start, stop, step = self.iterable_a, 15, -15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_a2(self):
        iterable, start, stop, step = self.iterable_a, 25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_a3(self):
        iterable, start, stop, step = self.iterable_a, 35, -35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_b1(self):
        iterable, start, stop, step = self.iterable_b, 15, -15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_b2(self):
        iterable, start, stop, step = self.iterable_b, 25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_b3(self):
        iterable, start, stop, step = self.iterable_b, 35, -35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_c1(self):
        iterable, start, stop, step = self.iterable_c, 15, -15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_c2(self):
        iterable, start, stop, step = self.iterable_c, 25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_positive_c3(self):
        iterable, start, stop, step = self.iterable_c, 35, -35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_a1(self):
        iterable, start, stop, step = self.iterable_a, 15, -15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_a2(self):
        iterable, start, stop, step = self.iterable_a, 25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_a3(self):
        iterable, start, stop, step = self.iterable_a, 35, -35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_b1(self):
        iterable, start, stop, step = self.iterable_b, 15, -15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_b2(self):
        iterable, start, stop, step = self.iterable_b, 25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_b3(self):
        iterable, start, stop, step = self.iterable_b, 35, -35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_c1(self):
        iterable, start, stop, step = self.iterable_c, 15, -15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_c2(self):
        iterable, start, stop, step = self.iterable_c, 25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_positive_negative_negative_c3(self):
        iterable, start, stop, step = self.iterable_c, 35, -35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    # -----------------------------------------------------------------------------------------------

    def test_negative_positive_positive_a1(self):
        iterable, start, stop, step = self.iterable_a, -15, 15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_a2(self):
        iterable, start, stop, step = self.iterable_a, -25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_a3(self):
        iterable, start, stop, step = self.iterable_a, -35, 35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_b1(self):
        iterable, start, stop, step = self.iterable_b, -15, 15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_b2(self):
        iterable, start, stop, step = self.iterable_b, -25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_b3(self):
        iterable, start, stop, step = self.iterable_b, -35, 35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_c1(self):
        iterable, start, stop, step = self.iterable_c, -15, 15, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_c2(self):
        iterable, start, stop, step = self.iterable_c, -25, 25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_positive_c3(self):
        iterable, start, stop, step = self.iterable_c, -35, 35, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_a1(self):
        iterable, start, stop, step = self.iterable_a, -15, 15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_a2(self):
        iterable, start, stop, step = self.iterable_a, -25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_a3(self):
        iterable, start, stop, step = self.iterable_a, -35, 35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_b1(self):
        iterable, start, stop, step = self.iterable_b, -15, 15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_b2(self):
        iterable, start, stop, step = self.iterable_b, -25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_b3(self):
        iterable, start, stop, step = self.iterable_b, -35, 35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_c1(self):
        iterable, start, stop, step = self.iterable_c, -15, 15, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_c2(self):
        iterable, start, stop, step = self.iterable_c, -25, 25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_positive_negative_c3(self):
        iterable, start, stop, step = self.iterable_c, -35, 35, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_a1(self):
        iterable, start, stop, step = self.iterable_a, -20, -30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_a2(self):
        iterable, start, stop, step = self.iterable_a, -25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_a3(self):
        iterable, start, stop, step = self.iterable_a, -30, -20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_b1(self):
        iterable, start, stop, step = self.iterable_b, -20, -30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_b2(self):
        iterable, start, stop, step = self.iterable_b, -25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_b3(self):
        iterable, start, stop, step = self.iterable_b, -30, -20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_c1(self):
        iterable, start, stop, step = self.iterable_c, -20, -30, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_c2(self):
        iterable, start, stop, step = self.iterable_c, -25, -25, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_positive_c3(self):
        iterable, start, stop, step = self.iterable_c, -30, -20, 3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_a1(self):
        iterable, start, stop, step = self.iterable_a, -20, -30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_a2(self):
        iterable, start, stop, step = self.iterable_a, -25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_a3(self):
        iterable, start, stop, step = self.iterable_a, -30, -20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_b1(self):
        iterable, start, stop, step = self.iterable_b, -20, -30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_b2(self):
        iterable, start, stop, step = self.iterable_b, -25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_b3(self):
        iterable, start, stop, step = self.iterable_b, -30, -20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_c1(self):
        iterable, start, stop, step = self.iterable_c, -20, -30, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_c2(self):
        iterable, start, stop, step = self.iterable_c, -25, -25, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)

    def test_negative_negative_negative_c3(self):
        iterable, start, stop, step = self.iterable_c, -30, -20, -3
        actual = list(utilitools.islice(iterable, start, stop, step))
        expected = list(range(50)[start:stop:step])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
