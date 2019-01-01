#!/usr/bin/env python3
def first_duplicate(arr):
    """first_duplicate(arr) --> the function return the first duplicated integer found, or -1 if not found
    --> Time complexity:  O(n) even in the worst case
    --> Space complexity: it takes O(k) where constant k <= 105. If our array length is a maximum of 105, then I would
     say the space complexity is O(1) or constant.
    --> But if the length of the array is unlimited, then it takes O(k) where k <= n which is O(n) at the worst case

    :param arr: An array of integers
    :return: the first duplicated integer found, or -1 if duplicated integer not found
    """
    s = set()
    for a in arr:
        if a in s:
            return a
        else:
            s.add(a)
    return -1


if __name__ == "__main__":
    print(first_duplicate([2, 3, 0, 1, 5, 2, 3]))
    print(first_duplicate([2, 3, 3, 1, 5, 2]))

    