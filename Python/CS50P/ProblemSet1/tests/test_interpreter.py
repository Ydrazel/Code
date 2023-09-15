#-*- code: utf-8 -*-
import unittest

class testInterpreter(unittest.TestCase):

    def testDivision(self):
        self.assertTrue(20 / 5 == 4.0)
        self.assertTrue(1 / 2 == 0.5)
        self.assertTrue(18 / 3 == 6.0)
        with self.assertRaises(ZeroDivisionError):
            15 / 0
    def testMultiplication(self):
        self.assertTrue(5 * 3 == 15.0)
        self.assertTrue(4 * 0 == 0.0)
        self.assertTrue(-2 * 3 == -6.0)
    def testAddition(self):
        self.assertTrue(4 + 8 == 12.0)
        self.assertTrue(-5 + -4 == -9.0)
        self.assertTrue(3 + 0 == 3.0)
    def testSubtraction(self):
        self.assertTrue(0 - 3 == -3.0)
        self.assertTrue(10 - 5 == 5.0)
        self.assertTrue(-5 + -7 == -12.0)

if __name__ == '__main__':
    unittest.main()
