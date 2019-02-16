"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""
""" Runtime: 24 ms, faster than 99.39% of Python online submissions for Factorial Trailing Zeroes.
"""
def factorial_trailing_zeroes(n):
    """ BIG TRICK: The trick is the combination of 2 and 5, 2 * 5, makes a TRAILING ZEROES. Since we have
    plenty of 2's, counting how many 5's we have in the factorial will tell us how many trailing zeroes we
    will have. Therefore divide the factorial with 5 and keep adding by dividing the RESULT AGAIN BY 5 until
    you get zero, and adding up all the RESULTS will give us the trailing zeroes.
    Here's the link:
    https://www.youtube.com/watch?v=wdz_KouqHx4
    """

    return 0 if n//5 == 0 else n//5 + factorial_trailing_zeroes(n//5)





print(factorial_trailing_zeroes(3))
print(factorial_trailing_zeroes(5))
