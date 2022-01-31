# Assingnment 1: Roman Numerals Kata

numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def convert_to_roman(input_number):
    range_flag = None
    for roman, integer in numerals.items():
        if integer == input_number:
            return roman
        if input_number > integer:
            range_flag = roman
    remaining = input_number - numerals[range_flag]
    return range_flag + convert_to_roman(remaining)


print(convert_to_roman(1111))
