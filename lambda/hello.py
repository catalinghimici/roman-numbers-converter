import re


class InvalidRomanNumeralError(Exception):
    pass


def handler(event, context):
    print('hello')


def roman_to_int(roman_number: str) -> int:
    validate_input(roman_number)


def validate_input(roman_number: str):
    if not roman_number:
        raise InvalidRomanNumeralError('Input can not be blank')
    if not isinstance(roman_number, str):
        raise InvalidRomanNumeralError('Input must be a string')
    if not re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_number):
        raise InvalidRomanNumeralError('Input is not a valid roman number')
