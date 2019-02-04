"""
32. Given an arr, get the permutations and combinations
"""
from itertools import permutations, combinations
def get_perm_comb(string, n):
    perms = permutations(string)
    combs = combinations(string, n)
    for p in perms:
        print(p)
    print("--------")
    for c in combs:
        print(c)









string = "abc"
n = 2
get_perm_comb(string, n)

