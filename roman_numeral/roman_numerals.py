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
        reduced_num = number
        #FIRST see if the number is in the dictionary
        for arabic_num, letter in roman_numeral_values.items():
            if number == arabic_num:
                convert += roman_numeral_values[number]
                #subtract the converted amount from the given number
                reduced_num -= arabic_num

        print(reduced_num)
           
        # except KeyError:
        

    
    return convert
    #pass the updated number into conversion
    # return convert and conversion(number-1)

print(conversion(number))
            