"""
Given a non-negative integer num, repeatedly add all its digits until the result has only
one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

def add_digits(num):

    while num > 9:
        lst = list(str(num))
        lst = [int(i) for i in lst]
        num = sum(lst)

    return num

print(add_digits(38))