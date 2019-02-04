"""
11. Get the highest safe floor(1 - 100) where eggs won't be broken with the minimal trial
"""


def highest_safe_floor(n, N):

    mid = (N - n) // 2

    if mid == "safe":
        n = mid
        return highest_safe_floor(n, N)
    else:
        N = mid
        return highest_safe_floor(n, N)






n = 0
N = 100
print(highest_safe_floor(n, N))