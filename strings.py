
str1 = 'aa'
str2 = 'ba'

def find_diff(str1, str2):
    if str1 is None or str2 is None:
        raise TypeError ("You can't have an empty string")







if len(str1) > len(str2):
    compare_string = str1[:len(str2)]
    for i, letter in enumerate(compare_string):
        if compare_string[i] != str2[i]:
            print(letter)
        

elif len(str1) < len(str2):
    compare_string = str2[:len(str1)]
    for i, letter in enumerate(compare_string):
        if compare_string[i] != str1[i]:
            print(letter)

else: 
    for i, letter in enumerate(str1):
        if compare_string[i] != str2[i]:
            print(letter)
        

