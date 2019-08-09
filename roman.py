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
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
}

number = 3
convert = []

def exact_match(roman_numeral_values):
    vals_to_extract = []

    for nums in roman_numeral_values.keys():
        converted_value = roman_numeral_values.get(number)

        if converted_value:
            vals_to_extract.append(converted_value)
            return vals_to_extract
    
numbers_to_extract = exact_match(roman_numeral_values)


multiple_five = [num for num in range(1, number+1) if num % 5 == 0]

def number_is_multiple_of_five():

    while True:
        if sum(convert) > number or sum(convert) == number:
            break
        
        if number - sum(convert) >= 10:
            convert.append(roman_numeral_values['X'])
        
        if number - sum(convert) == 5:
            convert.append(roman_numeral_values['V'])
    return convert


def number_not_multiple_of_five():
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
    
print(number_not_multiple_of_five())
    




# sorted_numbers_to_convert = sorted(nums_to_convert, reverse=True)



# number_to_roman_numeral = []
# for num in sorted_numbers_to_convert:
#     letter = roman_numeral_values.get(num)
#     number_to_roman_numeral.append(letter)


#     print(number_to_roman_numeral)




    















# def int_vals_to_extract(roman_numeral_values):

#     convert = 0
#     counts = []
#     for num in range(1, number+1):
#         if num in roman_numeral_values.keys():
#             counts.append(num)

     
# print(int_vals_to_extract(roman_numeral_values))

    # #Get the highest common val that's in the dictionary and then remove it
    # start_value = max(counts)
    # convert = start_value
    # counts.remove(start_value)

    # #cycle through the remaining common values
    # while convert < number:
    #     for value in counts:
    #         print(value)

        
        

    
    
 


      
        # else:
        #     common_nums = []
        #     for num in range(1, number+1):
        #         if num in roman_numeral_values.keys():
        #             common_nums.append(num)
        #     max_common_nums = max(common_nums)
        #     difference = number - max_common_nums
        #     print(difference)
            #cycle through the difference and add to the balance until sum to number // I'll need a container that's comparing to the given number
           

    
    # return sorted(vals_to_extract, reverse=True)









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



