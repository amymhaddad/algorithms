"""Given a roman numeral, find the integer equivalent"""

# roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 16


roman_numeral_values = {1: "I", 5: "V", 10: "X"}

def conversion(number):
    """Convert an Arabic number to its roman numeral equivalent"""
    
    if number == 0:
        return ""

    else:
        convert = []
        reduced_num = number

        if number % 5 == 0:
            try:
                convert.append(roman_numeral_values[number])
                reduced_num -= number
            except KeyError:
                convert.append(roman_numeral_values[10])
                reduced_num -= 10
            
            #try to get this value from dictionary
            #except KeyError
            #Then get the largest value from the dictionary
            
            # convert.append(roman_numeral_values[number])
            # reduced_num -= number
            return "".join(convert) + conversion(reduced_num)


        elif number % 5 != 0 and number > 5:
            import pdb; pdb.set_trace()
            remainder = number % 5
            multiple_of_five = roman_numeral_values[(number-remainder)]
            convert.append(multiple_of_five)

            return "".join(convert) + conversion(remainder)


        elif number < 5:
            reduced_num -= 1
            convert.append(roman_numeral_values[1])

        return "".join(convert) + conversion(reduced_num)


print(conversion(number))
