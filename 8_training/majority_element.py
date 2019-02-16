"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""
def majorityElement(nums):
    """
    Runtime: 48 ms, faster than 40.45% of Python online submissions for Majority Element.
    """
    from collections import Counter
    freq = Counter(nums)
    return max(freq.items(), key=lambda kv: kv[1])[0]

def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    dict = Counter(nums)
    for key in dict:
        if dict[key] > len(nums) / 2:
            return key


print(majorityElement([2,2,1,1,1,2,2]))
