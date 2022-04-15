import unittest
import src.python.basic as basic

class test_basic(unittest.TestCase):

    def test_import(self):
        self.assertEqual(basic.f(1), 0)

    def test_import2(self):
        self.assertEqual(basic.f(1), 0)

if __name__ == "__main__":
  unittest.main()