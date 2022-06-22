import unittest
import utilitools


class Singleton(metaclass=utilitools.singleton):
    ...


class Test(unittest.TestCase):
    def test_same_object(self):
        instance_x = Singleton()
        instance_y = Singleton()
        self.assertIs(instance_x, instance_y)


if __name__ == '__main__':
    unittest.main()
