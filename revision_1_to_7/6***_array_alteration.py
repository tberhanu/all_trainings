"""
6. Given an array of int, return another array of int where each elt substituted
 by all other elements multiplied each other except the one at that same index
 Ex. [1, 2, 3, 0] --> [0, 0, 0, 6]

"""
from functools import reduce

def array_elts_multiplied(arr):

    i = 0
    arr2 = []
    while i < len(arr):
        """ Remember there is NO WORRIES of INDEX out of RANGE when dealing with SLICING"""
        nums = arr[:i] + arr[i+1:]
        result = reduce(lambda a, b: a*b, nums)
        arr2.append(result)
        i = i + 1
    return arr2

print(array_elts_multiplied([1, 2, 3, 0]))
print(array_elts_multiplied([1, 2, 3, 2]))
print(array_elts_multiplied([1, 1, 6, 1]))