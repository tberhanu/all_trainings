"""
Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the absolute difference
between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def contains_nearby_duplicate(nums, k):
    """Runtime: 60 ms, faster than 38.62% of Python3 online submissions for Contains Duplicate II.

    Here we go: Construct an array of tuples holding both the NUM value and the corresponding INDEX,
    which takes O(n), and also sort it using the NUM as a key which also takes o(n log n).
    At last, traverse throught the array of tuples and do some ARRAY INDEXING and COMPARING which all
    takes O(1). Therefre we did it with O(n log n) which is much better than the above O(n**2)
"""
    nums = [(num, i) for i, num in enumerate(nums)]
    nums = sorted(nums, key=lambda kv: kv[0])
    i = 0
    while i < len(nums) - 1:
        num1, num2 = nums[i], nums[i+1]
        if num1[0] == num2[0] and abs(num1[1] - num2[1]) <= k:
            return True
        i = i + 1
    return False


def very_smart(nums, k):
    """Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Contains
    Duplicate II.
    WOW!! Look carefully what this code is doing...smart smart. Once if you get two equal
    numbers but the index range isn't qualified, just replace with the new one as there is
    no way the old one could qualify anymore as we are traversing through the array the index
    range is increasing.
"""

    dic = {}

    for i in range(len(nums)):
        current = nums[i]
        if current in dic and i - dic[current] <= k:  # {val : index}
            return True
        else:
            dic[current] = i

    return False


print(contains_nearby_duplicate([4,1,2,3,1,5], 3))
print(contains_nearby_duplicate([1, 0, 1, 1], 1))
print(contains_nearby_duplicate([1,2,3,1,2,3], 2))
print(contains_nearby_duplicate([1,2,3,1], 3))
