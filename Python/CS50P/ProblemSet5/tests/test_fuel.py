#-*- code: utf-8 -*-
import unittest
from fuel import convert
from fuel import gauge

class TestStringMethods(unittest.TestCase):
    def test_conversion(self):
        with self.assertRaises(ValueError):
            convert("12/10")
            convert("cat/1")
            convert("3/s")
        with self.assertRaises(ZeroDivisionError):
            convert("1/0")
            convert("10/0")
        self.assertEqual(convert("1/2"), 50)
        self.assertEqual(convert("1/3"), 33)
        self.assertEqual(convert("1/1"), 100)
        self.assertEqual(convert("1/1000"), 0)
        self.assertEqual(convert("0/1"), 0)
    def test_gauge(self):
        self.assertEqual(gauge(0), "'E'")
        self.assertEqual(gauge(100), "'F'")
        self.assertEqual(gauge(33), "33%")
        
if __name__ == "__main__":
    unittest.main()