def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n - 1 == 0:
        return x
    return x * myPow(x, n - 1)


print(myPow(2, 10))