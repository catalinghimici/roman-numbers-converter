import unittest
from hello import roman_to_int, InvalidRomanNumeralError


class FromRomanBadInput(unittest.TestCase):
    def test_no_input(self):
        """
        Conversion should fail when no input is provided
        """
        self.assertRaises(InvalidRomanNumeralError, roman_to_int, None)

    def test_input_is_not_string(self):
        """
        Conversion should fail when no input is not the correct format
        """
        for roman_number in ([], 1234, {'MC'}):
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number)

    def test_contains_wrong_characters(self):
        """
        Conversion should fail with strings that contain characters that are not part of roman numerals
        Allowed characters: I, V, X, L, D, C, M
        """
        for roman_number in ('M-', 'DIa', '1234', 'asd'):
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number)

    def test_too_many_repeated_numerals(self):
        """
        Conversion should fail with too many repeated numerals
        M, C, X, I can repeat 3 times
        D, L, V can only appear once
        """
        for roman_number in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number)

    def test_repeated_pairs(self):
        """
        Conversion should fail with repeated pairs of numerals
        """
        for roman_number in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number)

    def test_malformed_antecedent(self):
        """
        Conversion should fail with malformed antecedents
        """
        for roman_number in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                             'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number)

    def test_from_roman_case(self):
        """
        Conversion should only accept uppercase input
        """
        for roman_number in ('mmc', 'viii'):
            roman_to_int(roman_number.upper())
            self.assertRaises(InvalidRomanNumeralError, roman_to_int, roman_number.lower())

    def test_known_values(self):
        """
        Conversion should be successful and return correct result
        """
        for roman_number, arab_number in [('DCCC', 800), ('DCCLXXXII', 782), ('MCMXCI', 1991), ('I', 1)]:
            calculated_arab_number = roman_to_int(roman_number)
            self.assertEqual(arab_number, calculated_arab_number)


if __name__ == '__main__':
    unittest.main()
