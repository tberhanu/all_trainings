"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.
"""

def three_sum(nums):
    """ Works but Time Limit Exceeded """
    from itertools import combinations
    sorted_combs = [sorted(c) for c in combinations(nums, 3)]
    dict = {}
    filtered = [dict.setdefault("".join(str(c)), c) for c in sorted_combs if
                sum(c) == 0 and "".join(str(c)) not in dict]
    return filtered

def three_sum2(nums):
    """ Works, and better run time interval
    """
    arr = []
    nums = sorted(nums)
    i = 0
    while i < len(nums):
        if i != 0 and nums[i] == nums[i - 1]:
            i = i + 1
            continue
            # if nums[i] < 0 and nums[k] < 0 and nums[i] > 0 and nums[k] > 0:
            #     break
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if j != i + 1 and nums[j] == nums[j - 1]:
                j = j + 1
                continue

            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                arr.append([nums[i], nums[j], nums[k]])
                j = j + 1
                k = k - 1
            if sum > 0:
                k = k - 1
            if sum < 0:
                j = j + 1
        i = i + 1
    return arr


print(three_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([1, 1, -2]))
print(three_sum([-1,0,1,2,-1,-4]))
