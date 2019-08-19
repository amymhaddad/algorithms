num1 = 6
num2 = 4
#find the factors for each number, then get the max common factor (use set() intersection)

num1_factors = []
for num_outer in range(1, num1+1):
    for num_inner in range(1, num1):
        if num_outer * num_inner == num1:
            num1_factors.append(num_outer)
print(num1_factors)

