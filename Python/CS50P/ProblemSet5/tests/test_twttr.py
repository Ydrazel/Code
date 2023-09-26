#-*- code: utf-8 -*-
import unittest
from twttr import shorten

class TestStringMethods(unittest.TestCase):
    def test_shorten(self):
        self.assertEqual(shorten('hello'), 'hll')
        self.assertEqual(shorten('merhaba'), 'mrhb')
        self.assertEqual(shorten('1oopsie'), '1ps')
        self.assertEqual(shorten('Hello, WOrlD'), 'Hll, WrlD')
        self.assertEqual(shorten('TEST STRING'), 'TST STRNG')

if __name__ == "__main__":
    unittest.main()
