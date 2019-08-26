s = "UDDDUDUU"


letters = [letter for letter in s]

count_u = 0
count_d = 0
for letter in letters:
    if letter == "U":
        count_u += 1
    if letter == "D":
        count_d += 1

valley_count = 0

if count_u % count_d == 0:
    valley_count += 1

print(valley_count)
