""" https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
import heapq
def get_median(nums1, nums2):
    nums = list(heapq.merge(nums1, nums2))
    index = len(nums) // 2
    if len(nums) % 2 != 0:
        return nums[index]
    else:
        return (nums[index] + nums[index - 1]) / 2


print(get_median([1, 4], [2, 3, 5, 7]))
