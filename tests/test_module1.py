import unittest
from featurify import module1

class TestModule1(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(module1.hello(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
