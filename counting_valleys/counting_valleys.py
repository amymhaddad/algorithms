steps = "DDUUDDUDUUUD"


# letters = [letter for letter in s]

# count_u = 0
# count_d = 0

# for letter in letters:
#     if letter == "U":
#         count_u += 1
#     if letter == "D":
#         count_d += 1


# valley_count = 0

# if count_u % count_d == 0:
#     valley_count += 1

# print(valley_count)



letter_with_count = []

repeated_letters = ''

for i, letter in enumerate(steps):
    # if list is empty, then add a letter to it
    if not repeated_letters:
        repeated_letters += letter
    
    #if letter is in repeated_letters, then we have a repeated letter -- add it to the repeated_letters list
    elif letter in repeated_letters:
        repeated_letters += letter

    #letter is not in repeated_letters, then we have a new letter. 
    #Tally up the current repeated letters and their count and make the new -- unique -- letter the compariosn letter 
    elif letter not in repeated_letters:
        if len(repeated_letters) >= 2:
            letter_with_count.append(repeated_letters)
        repeated_letters = letter

print(letter_with_count)

# DD UU DD U   D UUU D
# 2D 2U 2D 1U 1D 3U