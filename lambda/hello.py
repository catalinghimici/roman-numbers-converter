import re


class InvalidRomanNumeralError(Exception):
    pass


def handler(event, context):
    print('hello')


def roman_to_int(roman_number: str) -> int:
    """
    Converts a roman number to arab equivalent
    :param roman_number: str representation of a roman number
    :return: int
    """
    validate_input(roman_number)
    roman_to_arab = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_number = replace_characters_that_should_be_subtracted(roman_number)

    number = 0
    for char in roman_number:
        number += roman_to_arab[char]
    return number


def replace_characters_that_should_be_subtracted(roman_number: str) -> str:
    """
    Changing the string to include only characters that should be added
    Note: the result is not a valid roman number
    :param roman_number: str representation of a roman number
    :return: str
    """
    roman_number = roman_number.replace("IV", "IIII").replace("IX", "VIIII")
    roman_number = roman_number.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_number = roman_number.replace("CD", "CCCC").replace("CM", "DCCCC")
    return roman_number


def validate_input(roman_number: str):
    """
    Validates that the provided roman number can be processed
    :param roman_number: str representation of a roman number
    :return: str
    """
    if not roman_number:
        raise InvalidRomanNumeralError('Input can not be blank')
    if not isinstance(roman_number, str):
        raise InvalidRomanNumeralError('Input must be a string')
    if not re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_number):
        raise InvalidRomanNumeralError('Input is not a valid roman number')
