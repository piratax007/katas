from unittest import TestCase

import roman_numerals_convert as rmc


class Test(TestCase):
    def test_verify_that_the_input_number_is_a_positive_integer(self):
        with self.assertRaises(ValueError):
            rmc.validate_input(-10)
        with self.assertRaises(ValueError):
            rmc.validate_input(3.141592)
        with self.assertRaises(ValueError):
            rmc.validate_input(4000)

    def test_convert_the_input_integer_to_a_string(self):
        self.assertEqual(1234, rmc.validate_input(1234))

    def test_separate_the_input_number_into_a_list_of_digits(self):
        self.assertListEqual([1, 2, 3, 4], rmc.separate_into_digits(1234))

    def test_convert_an_arabic_integer_to_roman_numeral(self):
        self.assertEqual("I", rmc.arabic_to_roman(1))
        self.assertEqual("V", rmc.arabic_to_roman(5))
        self.assertEqual("VII", rmc.arabic_to_roman(7))
        self.assertEqual("IX", rmc.arabic_to_roman(9))
        self.assertEqual("XXIII", rmc.arabic_to_roman(23))
        self.assertEqual("XXV", rmc.arabic_to_roman(25))
        self.assertEqual("XXIX", rmc.arabic_to_roman(29))
        self.assertEqual("XLV", rmc.arabic_to_roman(45))
        self.assertEqual("LXXXIX", rmc.arabic_to_roman(89))
        self.assertEqual("C", rmc.arabic_to_roman(100))
        self.assertEqual("DLXXXII", rmc.arabic_to_roman(582))
        self.assertEqual("MDCCLXXVI", rmc.arabic_to_roman(1776))
        self.assertEqual("MMCDXXI", rmc.arabic_to_roman(2421))
        self.assertEqual("MMMCMXCIX", rmc.arabic_to_roman(3999))
