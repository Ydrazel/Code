#-*- code: utf-8 -*-
import unittest
import emoji

class TestStringMethods(unittest.TestCase):

    def test_emojize(self):
        self.assertEqual(emoji.emojize(":1st_place_medal:", language="alias"), "🥇")
        self.assertEqual(emoji.emojize(":money_bag:", language="alias"), "💰")
        self.assertEqual(emoji.emojize(":smile_cat:", language="alias"), "😸")
        self.assertEqual(emoji.emojize(":Turkey:", language="alias"), "🇹🇷")

    def test_alias(self):
        self.assertEqual(emoji.emojize(":thumbsup:", language="alias"), "👍")
        self.assertEqual(emoji.emojize(":jp:", language="alias"), "🇯🇵") 
        self.assertEqual(emoji.emojize(":thumbsdown:", language="alias"), "👎")

if __name__ == "__main__":
    unittest.main()
