"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

"""
def max_subarray(nums):
    biggest = nums[0]
    i = 1
    while i < len(nums):
        sum = max(nums[i], nums[i-1] + nums[i])
        nums[i] = sum
        if sum > biggest:
            biggest = sum

        i = i + 1
    return biggest



print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) #6
