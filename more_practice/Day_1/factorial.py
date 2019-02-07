"""
4. Find factorial of a number
"""
from functools import reduce


def factorial(num):
    if num <= 1:
        return 1
    return reduce(lambda a, b: a * b, [i for i in range(2, num + 1)])


for num in range(11):
    print(factorial(num))

