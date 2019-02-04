#!/usr/bin/env python3
from functools import reduce

def products(arr):
    """products(arr) --> a function taking an array of integers, and gives out another array of integers, each of which
    are all the arr elements multiplied each other except the one at that same index

    :param arr: Array of integers
    :return: Array of integers
    """
    products = []
    for i in range(len(arr)):
        arr2 = arr[0:i] + arr[i+1:]
        result = reduce(lambda x, y: x * y, arr2)
        products.append(result)
    return products

if __name__ == "__main__":

    print(products([1, 7, 3, 4]))
    print(products([1, 2, 3, 0]))
