import unittest


class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M": 1000, "D": 500,
                          "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val


class RomanNumeralConverterTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_parsing_millenia(self):
        self.assertEqual(1000,
                         self.cvt.convert_to_decimal("M"))

    def test_parsing_century(self):
        self.assertEqual(100,
                         self.cvt.convert_to_decimal("C"))


class RomanNumeralComboTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_multi_millenia(self):
        self.assertEqual(4000,
                         self.cvt.convert_to_decimal("MMMM"))

    def test_multi_add_up(self):
        self.assertEqual(2010,
                         self.cvt.convert_to_decimal("MMX"))
