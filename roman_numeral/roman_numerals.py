"""Given a roman numeral, find the integer equivalent"""

# roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 15

roman_numeral_values = {1: "I", 5: "V", 10: "X"}


def conversion(number):
    """Convert an Arabic number to its roman numeral equivalent"""

    if number == 0:
        return ""

    else:
        convert = []
        reduced_num = number

        # First check: see if number is in dictionary. If so, return it, if not get the largest value from the dictionary
        if number % 5 == 0:
            try:
                convert.append(roman_numeral_values[number])
                reduced_num -= number
            except KeyError:
                convert.append(roman_numeral_values[10])
                reduced_num -= 10

            return "".join(convert) + conversion(reduced_num)

        # Second check: if the number is larger than 5, then subtract the remainder from the number and extract that result from the dictionary.
        if number > 5:
            try:
                remainder = number % 5
                multiple_of_five = roman_numeral_values[(number - remainder)]
                convert.append(multiple_of_five)
                reduced_num -= number - remainder
            except KeyError:
                convert.append(roman_numeral_values[10])
                reduced_num -= 10

            return "".join(convert) + conversion(reduced_num)

        elif number < 5:
            reduced_num -= 1
            convert.append(roman_numeral_values[1])

        return "".join(convert) + conversion(reduced_num)


print(conversion(number))
