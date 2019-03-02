"""
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise,
we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""


def maxRotateFunction(A):

    largest = sum(i * a for i, a in zip(range(len(A)), A))
    for i in range(1, len(A)):
        A[0:0] = [A.pop()]
        summed = sum(i * a for i, a in zip(range(len(A)), A))
        if summed > largest:
            largest = summed

    return largest

def mathematical_sol(A):
    """
    Once we get the curr value, for each circulation there are few adjustments need to calculate the
    new value:
    1. All indices increase by one except the last one so adding up the sum(A) minus A[-1] is good
    2. The value from the last number, A[-1]*(len(A)-1), should be subtracted
    3. Therefore adding up sum(A) and subtracting A[-1]*len(A) will give us the new value
    """
    highest = curr = sum(i * j for i, j in enumerate(A))
    summed = sum(A)
    length = len(A)
    while A:
        curr += summed - A.pop() * length
        highest = max(curr, highest)
    return highest


A = [4, 3, 2, 6]
print(maxRotateFunction(A))
print(mathematical_sol(A))