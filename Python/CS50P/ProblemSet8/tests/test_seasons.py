#-*- code: utf-8 -*-
import unittest
from seasons import get_date, convert

class TestSeasons(unittest.TestCase):
    def test_get_date(self):
        self.assertEqual(get_date("2022-10-18"), 525600)
        self.assertEqual(get_date("2021-10-18"), 1051200)
        with self.assertRaises(SystemExit):
            get_date("2022 10 18")
    def test_convert(self):
        self.assertEqual(convert(525600), "five hundred twenty-five thousand, six hundred minutes")
        self.assertEqual(convert(1051200), "one million, fifty-one thousand, two hundred minutes")

if __name__ == "__main__":
    unittest.main()
