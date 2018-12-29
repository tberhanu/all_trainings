#!/usr/bin/env python3.7

def remove_duplicates(arr):
    """

    :param arr: Array of integers
    :return: Tuple (of array of unique integers and it's length)
    """
    seen = set()
    arr2 = []
    for a in arr:
        if a in seen:
            continue
        else:
            arr2.append(a)
            seen.add(a)

    return arr2, len(arr2)

if __name__ == "__main__":

    print(remove_duplicates([1, 3, 3, 4, 5, 3, 8, 5]))
