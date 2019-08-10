
str1 = 'aaabbcdd'
str2 = 'abdbacade'


# def find_diff(str1, str2):
#     if str1 is None or str2 is None:
#         raise TypeError ("You can't have an empty string")


# letter_and_count_str1 = {}

# for letter in str1:
#     letter_and_count_str1[letter] = letter_and_count_str1.get(letter, 0) + 1


# letter_and_count_str2 = {}
# for letter in str2:
#     letter_and_count_str2[letter] = letter_and_count_str2.get(letter, 0) + 1



def find_diff(str1, str2):
    if len(str1) > len(str2):
        compare_string = str1[:len(str2)]
        for i, letter in enumerate(compare_string):
            if compare_string[i] != str2[i]:
                return letter 
            else:
                return str1[-1]
            

    elif len(str1) < len(str2):
        compare_string = str2[:len(str1)]
        for i, letter in enumerate(compare_string):
            if compare_string[i] != str1[i]:
                return letter
            else:
                return str2[-1]

    else: 
        for i, letter in enumerate(str1):
            if str1[i] != str2[i]:
                return letter

print(find_diff(str1, str2))