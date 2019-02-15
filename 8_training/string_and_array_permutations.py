""" Permutation for string which is relatively easier than that of permutation for arrays"""
def str_perms(string):
    return foo(string, "", [], len(string))

def foo(str, p, arr, n):
    if len(p) == n:
        arr.append(p)
    else:
        for i, s in enumerate(str):
            foo(str[:i] + str[i+1:], p + str[i], arr, n)
    return arr

# print(str_perms("abc"))
# print(str_perms("ab"))
# print(str_perms("abcd"))

#########################################################
def arr_perms(arr):
    start = 0
    result = []
    return permutation(arr, start, result)


def permutation(arr, start, result):
    """
    Recursion faith: This func gives the d/t permutations of the array by swapping the START index
    with all the indexes greater than or equal to itself, which means including ITSELF.
    [1,2,3], start=0
        p([1,2,3], start=1)
            p([1,2,3], start=2)
            p([1,3,2], start=2)
                [1,2,3] and [1,3,2] appended to the RESULT as start==len(arr)-1
        p([2,1,3], start=1)
            p([2,1,3], start=2)
            p([2,3,1], start=2)
                [2,1,3] and [2,3,1] appended to the RESULT as start==len(arr)-1
        p([3,2,1], start=1)
            p([3,2,1], start=2)
            p([3,1,2], start=2)
                [3,2,1] and [3,1,2] appended to the RESULT as start==len(arr)-1
    """
    if start == len(arr) - 1:
        result.append(arr[:])

    for i in range(start, len(arr)):
        swap(start, i, arr)
        permutation(arr, start + 1, result)
        swap(start, i, arr)
    return result


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


# print(arr_perms([1, 2, 3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permutationsII(arr):
    """
    Given a collection of numbers that might contain duplicates, return all possible unique
    permutations.
    This code works, but need a way to make it faster.
    """
    results = arr_perms(arr)
    filtered = []
    for i, result in enumerate(results):
        if result not in filtered:
            filtered.append(result)

    return filtered



print(permutationsII([1, 1, 2]))
# [[1, 1, 2],[1, 2, 1],[2, 1, 1]]
