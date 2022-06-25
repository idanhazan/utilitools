import unittest
import utilitools


class Singleton(metaclass=utilitools.singleton):
    ...


class Test(unittest.TestCase):
    def test_singleton(self):
        actual = Singleton()
        expected = Singleton()
        self.assertIs(expected, actual)


if __name__ == '__main__':
    unittest.main()
