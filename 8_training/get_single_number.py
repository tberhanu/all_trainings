"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def get_single_number(nums):
    """Your runtime beats 93.56 % of python3 submissions.
"""
    from collections import Counter
    freq = Counter(nums)
    arr = [k for k, v in freq.items() if v == 1]
    return arr[0]

def get_single_number_VERY_SLOW(nums):
    """Your runtime beats 1.23 % of python3 submissions.
"""
    for i in range(len(nums)):
        if nums[i] not in nums[:i] + nums[i+1:]:
            return nums[i]
    return False
