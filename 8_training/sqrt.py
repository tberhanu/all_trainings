"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer
part of the result is returned.


"""
def sqrt(num):
    start = 0
    end = (num // 2) + 1
    return foo(num, start, end)

def foo(num, start, end):

    while start < end:

        mid = (start + end) // 2
        square = mid * mid
        if square == num:
            return mid
        if square > num:
            end = mid - 1
        if square < num:
            start = mid + 1

    if start * start > num:
        return start - 1
    return start


print(sqrt(9))
print(sqrt(17))
