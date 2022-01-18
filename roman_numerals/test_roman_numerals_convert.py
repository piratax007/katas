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

    def test_separate_the_input_number_into_a_list_of_digits(self):
        self.assertEqual([0, 0, 0, 5], rmc.separate_into_digits(5))
        self.assertEqual([0, 0, 5, 7], rmc.separate_into_digits(57))
        self.assertEqual([0, 8, 5, 3], rmc.separate_into_digits(853))
        self.assertListEqual([1, 2, 3, 4], rmc.separate_into_digits(1234))

    def test_convert_an_arabic_integer_to_roman_numeral(self):
        self.assertEqual("I", rmc.roman_from(1))
        self.assertEqual("V", rmc.roman_from(5))
        self.assertEqual("VII", rmc.roman_from(7))
        self.assertEqual("IX", rmc.roman_from(9))
        self.assertEqual("XXIII", rmc.roman_from(23))
        self.assertEqual("XXV", rmc.roman_from(25))
        self.assertEqual("XXIX", rmc.roman_from(29))
        self.assertEqual("XLV", rmc.roman_from(45))
        self.assertEqual("LXXXIX", rmc.roman_from(89))
        self.assertEqual("C", rmc.roman_from(100))
        self.assertEqual("DLXXXII", rmc.roman_from(582))
        self.assertEqual("MDCCLXXVI", rmc.roman_from(1776))
        self.assertEqual("MMCDXXI", rmc.roman_from(2421))
        self.assertEqual("MMMCMXCIX", rmc.roman_from(3999))
