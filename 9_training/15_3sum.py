"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    """Runtime: 4140 ms, faster than 7.93% of Python3 online submissions for 3Sum.

    CAN YOU MAKE IT BETTER ????????
"""
    nums = sorted(nums)
    t = 0

    arr = []
    while t < len(nums):
        target = nums[t]
        i = t + 1
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if target + sum == 0:
                ordered = [nums[i], nums[j], target]
                if ordered not in arr:
                    arr.append(ordered)
                i = i + 1
                j = j - 1
            elif target + sum > 0:
                j = j - 1
            else:
                i = i + 1
        t = t + 1
    return arr

print(threeSum([-1, 0, 1, 2, -1, -4]))


