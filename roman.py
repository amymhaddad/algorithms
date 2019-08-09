"""Given a roman numeral, find the integer equivalent"""

roman_numeral_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
}

reversed_roman_to_arabic = dict(map(reversed, roman_numeral_values.items()))

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
    

numbers_to_convert = arabic_to_roman(number)

def conversion(numbers_to_convert):
    roman_numeral = []

    for num in numbers_to_convert:
        roman_numeral.append(reversed_roman_to_arabic.get(num))
    return "".join(roman_numeral)
     
print(conversion(numbers_to_convert))
