"""
18. Given 2 arrays A and B of equal size, the advantage of A with respect to B is the number
of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B
"""
from collections import deque


def shuffled_A(A, B):
    a = deque(sorted(A))
    b = deque(sorted(B))
    diff = sum(1 for a1, b1 in zip(a, b) if a1 - b1 > 0)
    lst_of_tuples = list(zip(b, a))
    if diff == len(A):
        arr = translate_back(lst_of_tuples, B)
        return arr
    else:
        largest = diff
        for i in range(len(A)-1):
            a.appendleft(a.pop())
            diff = sum(1 for a1, b1 in zip(a, b) if a1 - b1 > 0)
            if diff > largest:
                largest = diff
                lst_of_tuples = list(zip(b, a))

        arr = translate_back(lst_of_tuples, B)
        return arr

def translate_back(lst_of_tuples, B):
    arr = []
    for b in B:
        for i, tup in enumerate(lst_of_tuples):
            if b == tup[0]:
                arr.append(tup[1])
                del lst_of_tuples[i]
    return arr

A = [2, 0, 4, 1, 2]
B = [1, 3, 0, 0, 2]
print(shuffled_A(A, B))
# [2, 0, 1, 2, 4]

A = [2,7,11,15]
B = [1,10,4,11]
print(shuffled_A(A, B))
# output = [2,11,7,15]

A = [0]
B = [0]
print(shuffled_A(A, B))

A = [7, 3, 1, 5]
B = [4, 2, 6, 8]
print(shuffled_A(A, B))