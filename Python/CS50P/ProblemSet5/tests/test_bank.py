#-*- code: utf-8 -*-
import unittest
from bank import value

class TestStringMethods(unittest.TestCase):
    def test_100(self):
        self.assertEqual(value("what's up!"), "$100")
        self.assertEqual(value("Shalom"), "$100")
        self.assertEqual(value("Selam"),"$100")
        self.assertEqual(value("İyi günler"), "$100")
    def test_20(self):
        self.assertEqual(value("hi!"), "$20")
        self.assertEqual(value("Howdy!"), "$20")
        self.assertEqual(value("hella"), "$20")
    def test_0(self):
        self.assertEqual(value("hello"), "$0")
        self.assertEqual(value("hello, sir!"), "$0")
        self.assertEqual(value("Hello"), "$0")

if __name__ == "__main__":
    unittest.main()
