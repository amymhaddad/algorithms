
str1 = 'aab'
str2 = 'ab'

def find_diff(str1, str2):
    if str1 is None or str2 is None:
        raise TypeError ("You can't have an empty string")

    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len == str2_len:
        for i, letter in enumerate(str1):
            if str1[i] != str2[i]:
                return letter
    

# print(find_diff(str1, str2))

if len(str1) > len(str2):
    compare_string = str1[:len(str2)]
    for i, letter in enumerate(compare_string):
        if compare_string[i] != str2[i]:
            print(letter)

