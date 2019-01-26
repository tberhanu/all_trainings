""" https://leetcode.com/problems/contains-duplicate-iii/
220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices
i and j in the array such that the absolute difference between nums[i] and
nums[j] is at most t and the absolute difference between i and j is at most k.

** Passed the tests, but didn't meet the runtime requirement so need to refactor
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    if len(nums) == 1 or k == 0:
        return False
    for i in range(len(nums)):
        for j in range(1, k + 1):
            if i + j < len(nums) and abs(nums[i] - nums[i + j]) <= t:
                print(i, i + j)
                return True
    return False

nums = [1,5,9,1,5,9]
print(containsNearbyAlmostDuplicate(nums, 2, 3))
