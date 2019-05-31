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

    def test_parsing_half_century(self):
        self.assertEqual(50,
                         self.cvt.convert_to_decimal("L"))

    def test_parsing_decade(self):
        self.assertEqual(10,
                         self.cvt.convert_to_decimal("X"))

    def test_parsing_half_decade(self):
        self.assertEqual(5, self.cvt.convert_to_decimal("V"))

    def test_parsing_one(self):
        self.assertEqual(1, self.cvt.convert_to_decimal("I"))

    def test_empty_roman_numeral(self):
        self.assertTrue(self.cvt.convert_to_decimal("") == 0)
        self.assertFalse(self.cvt.convert_to_decimal("") > 0)

    def test_no_roman_numeral(self):
        self.assertRaises(TypeError,
                          self.cvt.convert_to_decimal, None)

    def test_combo1(self):
        self.assertEqual(4000,
                         self.cvt.convert_to_decimal("MMMM"))

    def test_combo2(self):
        self.assertEqual(2010,
                         self.cvt.convert_to_decimal("MMX"))

    def test_combo3(self):
        self.assertEqual(4668,
                         self.cvt.convert_to_decimal("MMMMDCLXVIII"))


def high_and_low():
    suite = unittest.TestSuite()
    suite.addTest(
        RomanNumeralConverterTest("test_parsing_millenia"))
    suite.addTest(
        RomanNumeralConverterTest("test_parsing_one"))
    return suite


def combos():
    return unittest.TestSuite(map(RomanNumeralConverterTest,
                                  ["test_combo1", "test_combo2",
                                   "test_combo3"]))


def all():
    return unittest.TestLoader().loadTestsFromTestCase(
        RomanNumeralConverterTest)


if __name__ == "__main__":
    for suite_func in [high_and_low, combos, all]:
        print("Running test suite '%s'" % suite_func.__name__)
        suite = suite_func()
        unittest.TextTestRunner(verbosity=2).run(suite)
