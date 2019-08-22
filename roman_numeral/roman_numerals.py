"""Given a roman numeral, find the integer equivalent"""

# roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 6


roman_numeral_values = {1: "I", 5: "V", 10: "X"}


# def multiples_of_five():
#     """Create a list of numbers that are multiples of 5"""
#     multiples = []
#     for nums in range(1, number + 1):
#         if nums % 5 == 0:
#             multiples.append(nums)
#     return multiples


def conversion(number):
    """Convert an Arabic number to its roman numeral equivalent"""
    if number == 0:
        return ""

    else:
        convert = []
        reduced_num = number

        if number % 5 == 0:
            convert.append(roman_numeral_values[number])
            reduced_num -= number
        else:
            reduced_num -= 1
            convert.append(roman_numeral_values[1])

    return "".join(convert) + conversion(reduced_num)


print(conversion(number))
