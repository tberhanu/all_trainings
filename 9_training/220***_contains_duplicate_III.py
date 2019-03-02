"""
Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute
difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


def containsNearbyAlmostDuplicate(nums, k, t):
    """Runtime: 60 ms, faster than 38.90% of Python3 online submissions for Contains Duplicate III.
"""
    zipped1 = sorted(list(zip(nums, range(len(nums)))))
    bool_one = foo(k, t, zipped1)
    return bool_one


def foo(k, t, zipped):
    i = 0
    while i < len(zipped) - 1:
        j = i + 1
        while j < len(zipped):
            val_interval = abs(zipped[i][0] - zipped[j][0])
            index_interval = abs(zipped[i][1] - zipped[j][1])
            if val_interval <= t and index_interval <= k:
                return True
            elif val_interval <= t:
                j = j + 1
            else:
                break
        i = i + 1

    return False


a = [-1, -1]
b = 1
c = 0
print(containsNearbyAlmostDuplicate(a, b, c)) #  True
nums = [1, 3, 6, 2]
k = 1
t = 2
print(containsNearbyAlmostDuplicate(nums, k, t)) #  True

print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)) # True
nums = [1,0,1,1]
k = 1
t = 2
print(containsNearbyAlmostDuplicate(nums, k, t)) # True
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(containsNearbyAlmostDuplicate(nums, k, t)) # False
a = [1,9,3,16,21,2]
b = 2
c = 2
print(containsNearbyAlmostDuplicate(a, b, c)) # True