"""
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):

    for i in range(len(nums)):
        if target - nums[i] in nums[:i] or target - nums[i] in nums[i + 1:]:
            save = nums[i]
            nums[i] = target - nums[i] + 99
            return (i, nums.index(target - save))


def twoSum(nums, target):

    d = dict()
    for i in range(len(nums)):
        num2 = target - nums[i]
        if num2 in d:
            return [d[num2], i]
        else:
            d[nums[i]] = i

    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 7, 11, 15], 18))
print(twoSum([2, 7, 11, 15, 3, 1], 3))
print(twoSum([3, 3], 6))
