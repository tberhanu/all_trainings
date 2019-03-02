"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares
of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: Happy Number, 19

Input: 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example: Non Happy Number, 200
2**2 + 0**2 + 0**2 = 4
4**2 = 16
1**2 + 6**2 = 37
3**2 + 7**2 = 58
5**2 + 8**2 = 89
8**2 + 9**2 = 145
1**2 + 4**2 + 5**2 = 42
4**2 + 2**2 = 20
2**2 + 0**2 = 4, loop back where we started so will loop forever


"""

def is_happy(n):

    sets = set()
    while n != 1:
        lst = list(str(n))
        result = sum(int(i) * int(i) for i in lst)
        if result in sets:
            return False
        sets.add(result)
        n = result
    return True




# print(calculate(19))
# print(calculate(202))

print(is_happy(19))
print(is_happy(200))