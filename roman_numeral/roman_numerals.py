"""Given a roman numeral, find the integer equivalent"""

roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 5


roman_numeral_values = {
    1: "I",
    5: "V",
    10: "X",
}

conversion = []

multiples = []
for nums in range(1, number +1):
    if nums % 5 == 0:
        multiples.append(nums)


def conversion(number):

    if number == 0:
        return ""

    else:
        convert = ''
        
        # if number in roman_numeral_values.keys():
        convert += roman_numeral_values[number]
        

    
    return convert

print(conversion(number))
            