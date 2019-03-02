"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def permute(nums):
    start = 0
    result = []
    return permutation(nums, start, result)


def permutation(arr, start, result):
    if start == len(arr) - 1:
        result.append(arr[:])

    for i in range(start, len(arr)):
        arr[i], arr[start] = arr[start], arr[i]
        permutation(arr, start + 1, result)
        arr[i], arr[start] = arr[start], arr[i]
    return result

#################################################

def permute_via_dfs(nums):
    arr = []
    all = []
    return dfs(nums, arr, all)


def dfs(nums, arr, all):

    if len(nums) == 0:
        all.append(arr)

    i = 0
    while i < len(nums):
        dfs(nums[:i] + nums[i+1:], arr + [nums[i]], all)
        i = i + 1

    return all

print(permute_via_dfs([1, 2, 3]))
print(permute([1, 2, 3]))

