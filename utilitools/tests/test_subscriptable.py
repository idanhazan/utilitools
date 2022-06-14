import typing
import unittest
import utilitools


@utilitools.subscriptable(tuple)
def digit_sum(n):
    return sum(map(int, str(n)))


@utilitools.subscriptable(list)
def fibonacci():
    a, b = 0, 1
    yield a
    while True:
        a, b = b, a + b
        yield a


class Test(unittest.TestCase):
    digit_sum: typing.Any
    fibonacci: typing.Any

    @classmethod
    def setUpClass(cls):
        cls.digit_sum = digit_sum
        cls.fibonacci = fibonacci

    @classmethod
    def tearDownClass(cls):
        del cls.digit_sum
        del cls.fibonacci

    def test_digit_sum_by_index(self):
        self.assertEqual(digit_sum[123], 6)

    def test_digit_sum_by_slice(self):
        self.assertEqual(digit_sum[10:20:3], (1, 4, 7, 10))

    def test_fibonacci_by_index(self):
        self.assertEqual(fibonacci[123], 22698374052006863956975682)

    def test_fibonacci_by_slice(self):
        self.assertEqual(fibonacci[10:20:3], [55, 233, 987, 4181])


if __name__ == '__main__':
    unittest.main()
