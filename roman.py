"""Given a roman numeral, find the integer equivalent"""

roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]
# integers = [num for num in range(1, 11)]

# roman = "X"

# def roman_to_int(roman):
#     """Convert a roman numeral to an integer"""

#     roman_to_int = dict(zip(roman_numerals, integers))
#     for num in roman:
#         return roman_to_int[num]
# print(roman_to_int(roman))

number = 6


roman_numeral_values = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
}

conversion = []

# for num in range(1, number+1):
#     if num % 5:
#         x = roman_numeral_values.get(num)


# multiples = []
# for nums in roman_numeral_values.keys():
#     if number % nums == 0 and nums > 1:
#         if nums == number:
#             value = roman_numeral_values.get(nums)
#                 multiples.append(value)
#         else:


vals_to_extract = []
for nums in roman_numeral_values.keys():
    if number % nums == 0 or number % nums == 1:
        vals_to_extract.append(nums)

