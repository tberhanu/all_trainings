""" 870. Advantage Shuffle
Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].
Return any permutation of A that maximizes its advantage with respect to B. """
# def foo(A, B):
#     d = dict(zip(sorted(B), sorted(A)))
#     arr = []
#     for b in B:
#         arr.append(d[b])
#     return arr

def advantageCount(A, B):
    from collections import deque, defaultdict

    a = deque(sorted(A))
    b = sorted(B)
    sum = -1
    best = []
    highest = len(A)
    for i in range(len(A)):
        diffs = [x - y for x, y in zip(a, b)]
        lst = list(filter(lambda e: e > 0, diffs))
        if len(lst) == highest:
            best = list(a)[:]
            break
        if len(lst) > sum:
            sum = len(lst)
            best = []
            best = list(a)[:]
        elt = a.pop()
        a.appendleft(elt)
    lst_tuples = list(zip(b, best))
    dict = {}
    d = defaultdict(lambda :[], dict)
    for t in lst_tuples:
        d[t[0]].append(t[1])
    r = []
    for b in B:
        r.append(d[b].pop())
    return r


A = [2, 0, 4, 1, 2]
B = [1, 3, 0, 0, 2]
print(advantageCount(A, B))

A = [2,7,11,15]
B = [1,10,4,11]
print(advantageCount(A, B))
# output = [2,11,7,15]
A = [0]
B = [0]
print(advantageCount(A, B))

A = [7, 3, 1, 5]
B = [4, 2, 6, 8]
print(advantageCount(A, B))
