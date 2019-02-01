from itertools import permutations, combinations

arr = [1, 2, 3, 4]
perms =  permutations(arr)
for p in perms:
    print(p)
print("----------")
combs = combinations(arr, 3)
for c in combs:
    print(c)