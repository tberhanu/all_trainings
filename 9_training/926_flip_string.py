"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""


def minFlipsMonoIncr2(S):
    """ Runtime: 5360 ms, faster than 5.14% of Python3 online submissions for Flip String to Monotone Increasing.

    CAN YOU MAKE IT BETTER ????
"""
    i = 0
    min_cost = float("inf")
    while i < len(S):
        left_cost = S[:i].count("1")
        right_cost = S[i+1:].count("0")
        cost = left_cost + right_cost
        if cost < min_cost:
            min_cost = cost
        i = i + 1

    return min_cost

def minFlipsMonoIncr(S):
    """Runtime: 92 ms, faster than 52.70% of Python3 online submissions for Flip String to Monotone Increasing.

    Here we use sth like MEMOIZATION as we RECYCLE our previous calculation to calculate the current
    calculation with a minimum cost.
"""
    i = 0
    min_cost = float("inf")
    left_cost = S[:i].count("1")
    right_cost = S[i + 1:].count("0")
    while i < len(S):
        if i != 0:
            left_cost = left_cost + int(S[i - 1])
            c = 1 if S[i] == "0" else 0
            right_cost = right_cost - c
        cost = left_cost + right_cost
        if cost < min_cost:
            min_cost = cost
        i = i + 1

    return min_cost


print(minFlipsMonoIncr("00110"))

print(minFlipsMonoIncr("010110"))
print(minFlipsMonoIncr("00011000"))