import unittest
import utilitools


class Singleton(unittest.TestCase):
    def test_by_instance(self):
        self.assertEqual(Class(), Class())

    def test_by_pointer(self):
        self.assertIs(Class(), Class())


class Class(metaclass=utilitools.Singleton):
    ...


if __name__ == '__main__':
    unittest.main()
