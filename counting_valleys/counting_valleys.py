steps = "DDUUDDUDUUUD"
# steps = "UDDDUDUU"

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

#At the end of the string, and will add in the repeated letters ONLY if there's multiple 
if len(repeated_letters) > 1:
    letter_with_count.append(repeated_letters)
print(letter_with_count)


# ['DD', 'UU', 'DD', 'UUU']

# [DDD, UU]

counter = 0

up_down_step = ''
for step_type in letter_with_count:
    if not up_down_step:
        up_down_step += step_type

    elif step_type in up_down_step:
        counter += 0

    else:
        counter += 1

print(counter)
    
     