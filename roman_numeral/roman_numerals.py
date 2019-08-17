"""Given a roman numeral, find the integer equivalent"""

roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 6


roman_numeral_values = {
    1: "I",
    5: "V",
    10: "X",
}

conversion = []

# multiples = []
# for nums in range(1, number +1):
#     if nums % 5 == 0:
#         multiples.append(nums)

def multiples_of_five():
    multiples = []
    for nums in range(1, number +1):
        if nums % 5 == 0:
            multiples.append(nums)
    return multiples

def conversion(number):
    if number == 0:
        return ''   

    else:
        convert = []
        reduced_num = number

        if number in multiples_of_five():
            convert.append(roman_numeral_values[number])
            reduced_num -= number
        else:
            reduced_num -= 1
            convert.append(roman_numeral_values[1])


    return "".join(convert) + conversion(reduced_num)
        
print(conversion(number))

#Next steps:
# -Get the converted nums to numerals to get in sorted order