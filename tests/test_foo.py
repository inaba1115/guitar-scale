import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1 + 1, 2)
