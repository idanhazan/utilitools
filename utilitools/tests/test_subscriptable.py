import unittest
import utilitools


class Subscriptable(unittest.TestCase):
    def test_digit_sum_by_index(self):
        self.assertEqual(digit_sum[123], 6)

    def test_digit_sum_by_slice(self):
        self.assertEqual(digit_sum[10:20:3], (1, 4, 7, 10))

    def test_fibonacci_by_index(self):
        self.assertEqual(fibonacci[123], 22698374052006863956975682)

    def test_fibonacci_by_slice(self):
        self.assertEqual(fibonacci[10:20:3], [55, 233, 987, 4181])


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


if __name__ == '__main__':
    unittest.main()
