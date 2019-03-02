"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generateParenthesis(n):

    string = ""
    arr = []
    l, r = n, n
    foo(string, arr, l, r)
    return arr

def foo(string, arr, l, r):

    if l == 0 and r == 0:
        arr.append(string)
    if l > 0:
        foo(string + "(", arr, l - 1, r)
    if r > l:
        foo(string + ")", arr, l, r - 1)

print(generateParenthesis(3))
