def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    # if n == 0:
    #     return 0
    #
    # from functools import  reduce
    # arr = [e for e in range(1, n + 1)]
    # factorial = reduce(lambda a, b: a * b, arr)
    # cntr = 0
    # while factorial % 10 == 0:
    #     cntr = cntr + 1
    #     factorial = factorial // 10
    # return cntr

    return 0 if n == 0 else n // 5 + trailingZeroes(n // 5)

print(trailingZeroes(10))