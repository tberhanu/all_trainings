#!/usr/bin/env python3.7
import unittest

def fib(n):
    """
    :param n: integer
    :return: the nth fibonnaci number

    """
    dict = {0: 0, 1: 1}
    return fibonnacci(n, dict)

def fibonnacci(n, dict):
    """

    :param n: integer
    :param dict: dictionary (used for memoization)
    :return: the nth fibonnaci number
    """

    if n in dict:
        return dict[n]
    else:
        dict[n] = fibonnacci(n - 1, dict) + fibonnacci(n - 2, dict)
        return dict[n]

# if __name__ == "__main__":
#
#     for i in range(100):
#         print (i, fib(i))
if __name__ == '__main__':
    unittest.main()
# def test_fib():
#     result = fib(3)
#     assert result == 2
#     result = fib(5)
#     assert result == 5
#     result = fib(10)
#     assert result == 55