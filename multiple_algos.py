
#gcd iteration 
num1 = 10
num2 = 3

def gcd(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    test_num = min_num
    
    while True:
        if max_num % test_num == 0 and min_num % test_num == 0:
            return test_num
            break
        test_num -= 1


#gcd recursion
def gcdRecur(a, b):
    biggest_num = max(a, b)
    smallest_num = min(a, b)

    if biggest_num == 0:
        return smallest_num
    elif smallest_num == 0:
        return biggest_num
    else: 
        remainder = biggest_num % smallest_num
        return gcdRecur(smallest_num, remainder)

# print(gcdRecur(12, 45))


#Focus on algo part of prime numbers:
num = 11
factors = []
for num_outer in range(1, num+1):
    for num_inner in range(1, num+1):
        if num_outer * num_inner == num:
            factors.append(num_outer)
if len(factors) == 2:
    print("prime")


#A second way to find prime numbers
factors = []
for i in range(1, num +1 ):
    if num % i == 0:
        factors.append(i)
if len(factors) == 2:
    print("prime")
        

    

#fib sequence
