"""Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9"""

def is_reordered_power_of_two(N):
    """Runtime: 44 ms, faster than 75.12% of Python3 online submissions for Reordered Power of 2.
"""
    if N == 1 or N == 2:
        return True
    r = 2
    for i in range(33):
        r = r * 2
        if sorted(str(r)) == sorted(str(N)):
            return True

    return False

def using_bit_manipulation(N):
    """Your runtime beats 45.77 % of python3 submissions.
"""
    return sorted(str(N)) in [sorted(str(1<<i)) for i in range(33)]
