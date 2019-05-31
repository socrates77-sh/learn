import unittest


class RomanNumeralConverter(object):
    def __init__(self):
        self.digit_map = {"M": 1000, "D": 500,
                          "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def convert_to_decimal(self, roman_numeral):
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        if val > 4000:
            raise Exception("We don't handle values over 4000")
        return val

    def convert_to_roman(self, decimal):
        if decimal > 4000:
            raise Exception("We don't handle values over 4000")

        val = ""
        mappers = [(1000, "M"), (500, "D"), (100, "C"),
                   (50, "L"), (10, "X"), (5, "V"), (1, "I")]
        for (mapper_dec, mapper_rom) in mappers:
            while decimal >= mapper_dec:
                val += mapper_rom
                decimal -= mapper_dec
        return val


class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_to_roman_bottom(self):
        self.assertEqual("I", self.cvt.convert_to_roman(1))

    def test_to_roman_below_bottom(self):
        self.assertEqual("", self.cvt.convert_to_roman(0))

    def test_to_roman_negative_value(self):
        self.assertEqual("", self.cvt.convert_to_roman(-1))

    def test_to_roman_top(self):
        self.assertEqual("MMMM",
                         self.cvt.convert_to_roman(4000))

    def test_to_roman_above_top(self):
        self.assertRaises(Exception,
                          self.cvt.convert_to_roman, 4001)

    def test_to_decimal_bottom(self):
        self.assertEqual(1, self.cvt.convert_to_decimal("I"))

    def test_to_decimal_below_bottom(self):
        self.assertEqual(0, self.cvt.convert_to_decimal(""))

    def test_to_decimal_top(self):
        self.assertEqual(4000,
                         self.cvt.convert_to_decimal("MMMM"))

    def test_to_decimal_above_top(self):
        self.assertRaises(Exception,
                          self.cvt.convert_to_decimal, "MMMMI")

    def test_to_roman_tier1(self):
        self.assertEqual("V", self.cvt.convert_to_roman(5))

    def test_to_roman_tier2(self):
        self.assertEqual("X", self.cvt.convert_to_roman(10))

    def test_to_roman_tier3(self):
        self.assertEqual("L", self.cvt.convert_to_roman(50))

    def test_to_roman_tier4(self):
        self.assertEqual("C", self.cvt.convert_to_roman(100))

    def test_to_roman_tier5(self):
        self.assertEqual("D", self.cvt.convert_to_roman(500))

    def test_to_roman_tier6(self):
        self.assertEqual("M",
                         self.cvt.convert_to_roman(1000))

    def test_to_roman_bad_inputs(self):
        # self.assertEqual("", self.cvt.convert_to_roman(None))
        self.assertEqual("I", self.cvt.convert_to_roman(1.2))

    def test_to_decimal_bad_inputs(self):
        self.assertRaises(TypeError,
                          self.cvt.convert_to_decimal, None)
        self.assertRaises(TypeError,
                          self.cvt.convert_to_decimal, 1.2)


if __name__ == "__main__":
    unittest.main()
