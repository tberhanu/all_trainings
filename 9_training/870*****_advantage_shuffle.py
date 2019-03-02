"""Given two arrays A and B of equal size, the advantage of A with respect to B
is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
def advantageCount(A, B):
    """ Sometimes we OVERTHINK, and other times we lose our track and only think about how
    to CODE, but remember we CODE to solve our HUMAN PROBLEM so first think how you would
    do it MANUALLY without using computer. How would you make it faster manually? Once you
    get the idea, you may use it with the help of computer....code it"""

    A = sorted(A, reverse=True)
    arr = [None] * len(A)
    for b, index in sorted(zip(B, range(len(B))), reverse=True):
        if A[0] > b:
            arr[index] = A.pop(0)
        else:
            arr[index] = A.pop()

    return arr


def advantageCount_smart(A, B):
    A.sort()
    res = [None] * len(A)
    for a, b in sorted([(n, i) for i, n in enumerate(B)])[::-1]:
        if a < A[-1]:
            res[b] = A.pop()
        else:
            res[b] = A.pop(0)
    return res



A = [2,7,11,15]
B = [1,10,4,11]
print(advantageCount(A, B))
A = [12,24,8,32]
B = [13,25,32,11]
print(advantageCount(A, B))
A = [8, 2, 4, 4, 5, 6, 6, 0, 4, 7]
B = [0, 8, 7, 4, 4, 2, 8, 5, 2, 0]
print(advantageCount(A, B))

