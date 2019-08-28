"""Count the number of valleys Gary, a hiker, traverses."""

steps = "DDUUDDUDUUUD"


def find_repeated_letters(steps):
    """Return a list of repeated letters
    -- if the repeated letters appear side-by-side"""

    letter_with_count = []
    repeated_letters = ""

    for letter in steps:
        if not repeated_letters:
            repeated_letters += letter

        elif letter in repeated_letters:
            repeated_letters += letter

        elif letter not in repeated_letters:
            if len(repeated_letters) >= 2:
                letter_with_count.append(repeated_letters)
            repeated_letters = letter

    if len(repeated_letters) > 1:
        letter_with_count.append(repeated_letters)
    return letter_with_count


repeated_letters = find_repeated_letters(steps)


def count_valleys(repeated_letters):
    """Count the number of valleys from the repeated letter list.
    A valley has an equal or greater number of up steps as down steps."""

    counter = 0
    up_down_step = ""
    for step_type in repeated_letters:
        if not up_down_step:
            up_down_step += step_type

        elif step_type in up_down_step:
            counter += 0

        else:
            counter += 1

    return counter


print(count_valleys(repeated_letters))
