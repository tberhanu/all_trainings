"""
Given an array 1) select the unique elements 2) select the non unique elements

"""

def get_uniques(arr):

    dict = {}
    uniques = [dict.setdefault(kv, kv) for kv in arr if kv not in dict]
    return uniques



def get_non_uniques(arr):


    non_uniques = [a for i, a in enumerate(arr) if a not in arr[:i] and a not in arr[i+1:]]
    return non_uniques

def get_non_uniques_from_sorted(arr):


    non_uniques = set([a for i, a in enumerate(arr) if i + 1 < len(arr) and a == arr[i+1]])
    return non_uniques

def get_first_repeated_elt(arr):


    for a, b in zip(arr, arr[1:]):
        if a == b:
            return a
    return -1


print(get_uniques([1, 2, 3, 4, 3, 5, 2]))


print(get_non_uniques([1, 2, 3, 4, 3, 5, 2]))


print(get_non_uniques_from_sorted([1, 2, 2, 3, 3, 4, 5]))


print(get_first_repeated_elt([1, 2, 12, 3, 3, 4, 5]))
