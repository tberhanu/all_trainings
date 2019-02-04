"""
13. Given a nested array, return a flattened version of it.
Ex. [1, 2, [3, [4, 5], 6]] ---> [1, 2, 3, 4, 5, 6]
"""
from collections.abc import Iterable

def flatten(arr):

    for a in arr:
        if isinstance(a, Iterable):
            yield from flatten(a)
        else:
            yield a










print(list(flatten([1, 2, [3, [4, 5], 6]])))