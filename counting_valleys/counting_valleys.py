steps = "DDUUDDUDUUUD"
# steps = "UDDDUDUU"

letter_with_count = []
repeated_letters = ''

for i, letter in enumerate(steps):
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


counter = 0
up_down_step = ''
for step_type in letter_with_count:
    # if the type of step (up or down) is not in the empty string, then ad it
    if not up_down_step:
        up_down_step += step_type

    #If the types of steps are the same, don't touch the count -- i'm not traversing a valley
    elif step_type in up_down_step:
        counter += 0

    #The types of steps are differnet (ie, i go down then I go up -- so I count it as a valley)
    else:
        counter += 1

print(counter)
    
     