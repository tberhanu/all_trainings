"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

"""
from itertools import permutations
def letter_combs(digits):
    """Runtime: 36 ms, faster than 68.38% of Python3 online submissions for Letter Combinations of a Phone Number.
"""
    dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    if digits == "":
        return []
    arr = [dict[e] for e in digits]
    # print(arr)
    if len(digits) == 1:
        return list(arr[0])
    all = []
    index = 0
    string = ""
    return foo(arr, all, index, string)

def foo(arr, all, index, string):
    if len(string) == len(arr):
        all.append(string)

    i = 0
    while index < len(arr) and i < len(arr[index]):
        foo(arr, all, index + 1, string + arr[index][i])
        i = i + 1

    return all


print(letter_combs("2345"))
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
print(letter_combs("23"))








