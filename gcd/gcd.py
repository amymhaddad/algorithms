num1 = 12
num2 = 6
test_num = num2
#find the factors for each number, then get the max common factor (use set() intersection)

num1_factors = []
for num_outer in range(1, num1+1):
    for num_inner in range(1, num1):
        if num_outer * num_inner == num1:
            num1_factors.append(num_outer)

num2_factors = []
for num_outer in range(1, num2+1):
    for num_inner in range(1, num2):
        if num_outer * num_inner == num2:
            num2_factors.append(num_outer)

gcd = max(set(num1_factors) & set(num2_factors))


def gdc(num1, num2):
    if num1 % test_num == 0 and num2 % test_num == 0:
        return test_num
    else:
        test_num -= 1
    
    