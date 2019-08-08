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



roman_numeral_values = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
}

number = 14

#Write an algo that gets the mutliples for 5, 10, 4, 9. Then, cycle through given number and see if there are any multiples matches
#Then match the multiples 


def int_vals_to_extract(roman_numeral_values):
    vals_to_extract = []

    for nums in roman_numeral_values.keys():
        converted_value = roman_numeral_values.get(number)

        if converted_value:
            vals_to_extract.append(converted_value)
            return vals_to_extract
        
        else:
            common_nums = []
            for num in range(1, number+1):
                if num in roman_numeral_values.keys():
                    common_nums.append(num)
            max_common_nums = max(common_nums)
            difference = number - max_common_nums
            print(difference)
            #cycle through the difference and add to the balance until sum to number // I'll need a container that's comparing to the given number
           

    
    return sorted(vals_to_extract, reverse=True)

numbers_to_extract = int_vals_to_extract(roman_numeral_values)

print(numbers_to_extract)





def convert(numbers_to_extract):
    roman_value = []
    for int_val in numbers_to_extract:
        roman_value.append(roman_numeral_values.get(int_val))

    return "".join(roman_value)

# print(convert(numbers_to_extract))




#extra

# if number % nums == 0 or number % nums == 1:
#     vals_to_extract.append(nums)





#try, except version 
# to_extract(roman_numeral_values):
#     vals_to_extract = []

#     for nums in roman_numeral_values.keys():
#         try:
#             converted_value = roman_numeral_values.get(number)
    
#         except:
#             if number % nums == 0 or number % nums == 1:
#                 vals_to_extract.append(nums)
        
#         else:
#             vals_to_extract.append(converted_value)
#             return vals_to_extract

#     return sorted(vals_to_extract, reverse=True)

# numbers_to_extract = int_vals_to_extract(roman_numeral_values)



