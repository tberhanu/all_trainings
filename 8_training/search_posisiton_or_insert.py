"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        # Here's the trick of getting the mid, use '+' not '-'
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    """ Here we assume there is no duplicate in the array, otherwise the following couple
    of line codes won't work or need more work than this"""
    if left == right and nums[left] < target:
        return left + 1
    return left


print(search_insert([1,3,5,6], 5))
#2
print(search_insert([1,3,5,6], 2))
#1
print(search_insert([1,3,5,6], 7))
#4
print(search_insert([1,3,5,6], 0))
#0
