def minFlipsMonoIncr(S):
    """
    :type S: str
    :rtype: int
    """
    arr = []
    left = 0
    total = sum(int(s) for s in S)
    right = total
    for i, s in enumerate(S):
        if i == 0:
            left_ones = 0
        else:
            left_ones = left + int(S[i-1])
        left = left_ones
        if i == len(S) - 1:
            right_ones = 0
        else:
            right_ones = right - int(S[i+1])
        right_zeroes = len(S[i + 1:]) - right_ones
        right = right_ones

        total_switch = left_ones + right_zeroes
        arr.append(total_switch)
    return min(arr)


print(minFlipsMonoIncr("11011"))