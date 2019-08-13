"""Write a program that prints a staircase of size n."""

n = 4


def staircase(n):
    for number in range(1, n + 1):
        print("#" * number)


print(staircase(n))
