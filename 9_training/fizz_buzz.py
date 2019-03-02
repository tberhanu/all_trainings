"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both three
and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

def fizz_buzz(n):
    arr = [str(i+1) for i in range(n)]
    for i in range(2, n, 3):
        arr[i] = "Fizz"
    for i in range(4, n, 5):
        arr[i] = "Buzz"
    for i in range(14, n, 15):
        arr[i] = "FizzBuzz"
    return arr
print(fizz_buzz(15))

