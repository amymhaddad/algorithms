"""Given a roman numeral, find the integer equivalent"""

roman_numeral_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
}

number = 8
convert = []


def arabic_to_roman(number):
    if number in multiple_five(number):
        return number_is_multiple_of_five(number)
    else:
        return number_not_multiple_of_five(number)


def multiple_five(number):
    return [num for num in range(1, number+1) if num % 5 == 0]

    
def number_is_multiple_of_five(number):

    while True:
        if sum(convert) > number or sum(convert) == number:
            break
        
        if number - sum(convert) >= 10:
            convert.append(roman_numeral_values['X'])
        
        if number - sum(convert) == 5:
            convert.append(roman_numeral_values['V'])
    return convert


def number_not_multiple_of_five(number):
    while True:
        if sum(convert) > number or sum(convert) == number:
            break

        if number - sum(convert) >= 10:
            convert.append(roman_numeral_values['X'])
    
        if number - sum(convert) < 10 and number - sum(convert) > 5:
            convert.append(roman_numeral_values['V'])
        
        if number - sum(convert) < 5:
            convert.append(roman_numeral_values['I'])
    
    return convert
    

    




# def exact_match(roman_numeral_values):
#     vals_to_extract = []

#     for nums in roman_numeral_values.keys():
#         converted_value = roman_numeral_values.get(number)

#         if converted_value:
#             vals_to_extract.append(converted_value)
#             return vals_to_extract
    
# numbers_to_extract = exact_match(roman_numeral_values)
