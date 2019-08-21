num1 = 24
num2 = 1

num1_factors = []
for num_outer in range(1, num1+1):
    for num_inner in range(1, num1):
        if num_outer * num_inner == num1:
            num1_factors.append(num_outer)

import pdb; pdb.set_trace()
num2_factors = []
for num_outer in range(1, num2+1):
    for num_inner in range(1, num2):
        if num_outer * num_inner == num2:
            num2_factors.append(num_outer)



gcd = max(set(num1_factors) & set(num2_factors))