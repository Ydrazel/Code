#-*- code: utf-8 -*-
import unittest
from plates import is_valid

class TestStringMethods(unittest.TestCase):
    def test_length(self):
        self.assertTrue(is_valid("AA1122"))
        self.assertTrue(is_valid("aa"))
        self.assertTrue(is_valid("CS50"))
        self.assertFalse(is_valid("A"))
        self.assertFalse(is_valid(""))
        self.assertFalse(is_valid("aabbccd"))
    def test_firstTwoChars(self):
        self.assertTrue(is_valid("AA"))
        self.assertFalse(is_valid("1A"))
        self.assertFalse(is_valid("11"))
        self.assertFalse(is_valid("A1"))
    def test_digitUse(self):
        self.assertTrue(is_valid("aa10"))
        self.assertFalse(is_valid("aa01"))
        self.assertFalse(is_valid("aa11bb"))
    def test_type(self):
        self.assertFalse(is_valid(".aa"))
        self.assertFalse(is_valid("aa_bb"))
        self.assertFalse(is_valid("aabb!"))
    def test_valid(self):
        self.assertTrue(is_valid("CS50"))
        self.assertTrue(is_valid("aa11"))
        self.assertTrue(is_valid("ALLOK"))

if __name__ == "__main__":
    unittest.main()
