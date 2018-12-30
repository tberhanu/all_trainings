#!/usr/bin/env python3
def first_duplicate(arr):
    """first_duplicate(arr) --> the function return the first duplicated integer found, or -1 if not found
    --> Time complexity:  O(n)
    --> Space complexity: O(n) ONLY in the WORST CASE
    N.B. I am still trying to come up with constant space complexity O(1) at all times, so let me know if come up with
    one solution with O(1).

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