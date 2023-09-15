#-*- code: utf-8 -*-
import unittest

class TestCoke(unittest.TestCase):
    def testCoin(self):
        self.assertFalse(coin == 35)
        self.assertFalse(coin == 15)
        self.assertTrue(coin == 25)
        self.assertTrue(coin == 10)

if __name__ == "__main__":
    unittest.main()
