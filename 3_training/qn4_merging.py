#!/usr/bin/env python3

def merge(arr1, arr2):
    return sorted(arr1 + arr2)

if __name__ == "__main__":
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]
    merged = my_list + alices_list
    print(sorted(merged))

