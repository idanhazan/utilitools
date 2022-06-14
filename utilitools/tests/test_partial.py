import typing
import unittest
import utilitools


class Test(unittest.TestCase):
    isinstance_int: typing.Any
    isinstance_str: typing.Any

    @classmethod
    def setUpClass(cls):
        cls.isinstance_int = utilitools.partial(isinstance, ..., int)
        cls.isinstance_str = utilitools.partial(isinstance, ..., str)

    @classmethod
    def tearDownClass(cls):
        del cls.isinstance_int
        del cls.isinstance_str

    def test_isinstance(self):
        self.assertEqual(all(map(self.isinstance_int, [1, 2])), True)
        self.assertEqual(all(map(self.isinstance_int, ['1', 2])), False)
        self.assertEqual(all(map(self.isinstance_int, [1, '2'])), False)
        self.assertEqual(all(map(self.isinstance_int, ['1', '2'])), False)

        self.assertEqual(all(map(self.isinstance_str, [1, 2])), False)
        self.assertEqual(all(map(self.isinstance_str, ['1', 2])), False)
        self.assertEqual(all(map(self.isinstance_str, [1, '2'])), False)
        self.assertEqual(all(map(self.isinstance_str, ['1', '2'])), True)

        self.assertEqual(any(map(self.isinstance_int, [1, 2])), True)
        self.assertEqual(any(map(self.isinstance_int, ['1', 2])), True)
        self.assertEqual(any(map(self.isinstance_int, [1, '2'])), True)
        self.assertEqual(any(map(self.isinstance_int, ['1', '2'])), False)

        self.assertEqual(any(map(self.isinstance_str, [1, 2])), False)
        self.assertEqual(any(map(self.isinstance_str, ['1', 2])), True)
        self.assertEqual(any(map(self.isinstance_str, [1, '2'])), True)
        self.assertEqual(any(map(self.isinstance_str, ['1', '2'])), True)


if __name__ == '__main__':
    unittest.main()
