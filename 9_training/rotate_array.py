""" Given an array, rotate the array to the right by k steps, where k is non-negative. """
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.

    Runtime: 40 ms, faster than 96.04% of Python online submissions for Rotate Array.

    """
    k = k % len(nums)
    """ Here's how to INSERT multiple elements at the beginning of the array """
    nums[0:0] = nums[len(nums) - k:]
    del nums[len(nums) - k:] # Confused? Remember len(nums) is not fixed

    return nums

def rotate2(nums, k):
    k = k % len(nums)
    for i in range(k):
        nums.insert(0, nums[-1])
        del nums[-1]
    return nums



print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([1, 2, 3, 4, 5, 6, 7], 7))
print(rotate([1, 2, 3, 4, 5, 6, 7], 8))
print(rotate([1, 2, 3, 4, 5, 6, 7], 9))
