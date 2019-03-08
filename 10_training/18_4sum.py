"""Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

def four_sum(nums, target):
    """Runtime: 1188 ms, faster than 27.05% of Python3 online submissions for 4Sum.
"""
    nums.sort()
    all = set()
    size = len(nums)
    for i in range(size - 3):
        for j in range(i + 1, size - 2, 1):
            k = j + 1
            kk = size - 1
            s = nums[i] + nums[j]
            while k < kk:
                s2 = nums[k] + nums[kk]
                if s + s2 == target:
                    all.add((nums[i], nums[j], nums[k], nums[kk]))
                    k += 1
                    kk -= 1

                if s + s2 < target:
                    k += 1
                if s + s2 > target:
                    kk -= 1

    return [list(e) for e in all]


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(four_sum(nums, target))
