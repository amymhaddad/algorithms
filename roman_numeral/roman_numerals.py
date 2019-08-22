"""Given a roman numeral, find the integer equivalent"""

# roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IV", "X"]


number = 6


roman_numeral_values = {1: "I", 5: "V", 10: "X"}

def conversion(number):
    """Convert an Arabic number to its roman numeral equivalent"""
    
    if number == 0:
        return ""

    else:
        convert = []
        reduced_num = number

    #IF a number is a multiple of 5
        if number % 5 == 0:
            #Extract the multiple of 5 from the dictionary and add it to the converted list
            convert.append(roman_numeral_values[number])
            #Reduce the number by the amount of that number (in order to go back through and get the remaining values.)
            reduced_num -= number

        elif number > 5:
            remainder = number % 5
            multiple_of_five = roman_numeral_values[(number-remainder)]
            convert.append(multiple_of_five)
            
            return "".join(convert) + conversion(remainder)


        elif number < 5:
            #If number is not a multiple of 5, then reduce the number by 1 and add that value to the converted list
            reduced_num -= 1
            convert.append(roman_numeral_values[1])

        return "".join(convert) + conversion(reduced_num)


print(conversion(number))
