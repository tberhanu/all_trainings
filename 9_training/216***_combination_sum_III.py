"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers
from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


def combinationSum3(k, n):
    """Runtime: 5812 ms, faster than 5.24% of Python3 online submissions for Combination Sum III.
"""
    tup = ()
    all = set()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    foo(k, n, tup, all, arr)
    array = []
    for a in all:
        if len(list(a)) == len(set(a)):
            array.append(list(a))
    return array

def foo(k, n, tup, all, arr):

    if len(tup) == k and n == 0:
        all.add(tuple(sorted(tup)))
    elif len(tup) == k:
        return
    else:

        for i in range(1, len(arr) + 1):
            foo(k, n - i, tup + (i, ), all, arr[:i] + arr[i+1:])

######################################

def combinationSum33(self, k, n):
    """ Your runtime beats 31.07 % of python submissions.
"""
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    store = []
    bigStore = []
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    depth = 0
    return self.comb_sum(k, n, store, nums, depth, bigStore)

def comb_sum(self, k, n, store, nums, depth, bigStore):
    if depth == k and sum(store) == n:
        bigStore.append(store)
        return
    j = 0
    while j < len(nums):
        save = store[:]
        store.append(nums[j])
        nums2 = nums[j + 1:]
        self.comb_sum(k, n, store, nums2, depth + 1, bigStore)
        store = save[:]
        j = j + 1

    return bigStore


print(combinationSum3(3, 28))
