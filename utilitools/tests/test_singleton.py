import typing
import unittest
import utilitools


class Singleton(metaclass=utilitools.singleton):
    ...


class Test(unittest.TestCase):
    instance_x: typing.Any
    instance_y: typing.Any

    @classmethod
    def setUpClass(cls):
        cls.instance_x = Singleton()
        cls.instance_y = Singleton()

    @classmethod
    def tearDownClass(cls):
        del cls.instance_x
        del cls.instance_y

    def test_same_object(self):
        self.assertIs(self.instance_x, self.instance_y)


if __name__ == '__main__':
    unittest.main()
