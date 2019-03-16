""" Get the element not repeated more than k times"""

def unique(arr, k):
    """ Doc Doc."""
    for i, a in enumerate(arr):
        if arr.count(a) < k:
            return a



arr = [1, 2, 1, 2, 1, 2, 3, 3, 4, 4, 4]

print(unique(arr, 3))


print(unique.__doc__)