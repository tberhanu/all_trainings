"""
8. Inplace reverse an array of characters
"""

def inplace_reverse(arr):

    i = 0
    j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1

    return arr


print(inplace_reverse([1, 2, 3, 4]))
print(inplace_reverse([1, 2, 3, 4, 5]))