"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    tup = ()
    all = set()
    dfs(nums, tup, all)
    arr = []
    for tup in all:
        arr.append(list(tup))
    return arr




def dfs(nums, tup, all):

    if len(nums) == 0:
        all.add(tup)

    i = 0
    while i < len(nums):
        dfs(nums[:i] + nums[i+1:], tup + (nums[i], ), all)
        i = i + 1



print(permuteUnique([1, 1, 2]))
print(permuteUnique([1, 2, 3]))