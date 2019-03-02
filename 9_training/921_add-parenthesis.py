"""
Given a string S of '(' and ')' parentheses, we add the minimum number of
parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the
resulting string valid.

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4


Note:

S.length <= 1000
S only consists of '(' and ')' characters.

"""


def minAddToMakeValid2(S):
    """Runtime: 44 ms, faster than 43.37% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""
    S = list(S)
    i = 1
    while i < len(S):
        if i - 1 >= 0 and S[i-1] + S[i] == "()":
            del S[i]
            del S[i - 1]
            i = max(0, i - 2)
        else:
            i = i + 1
    return len(S)

def minAddToMakeValid(S):
    """Runtime: 40 ms, faster than 55.65% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""
    open, close = 0, 0
    for s in S:
        if s == "(":
            open += 1
        else:
            if open:
                open -= 1
            else:
                close += 1
    return open + close






print(minAddToMakeValid("(()())(("))
print(minAddToMakeValid("()))(("))
print(minAddToMakeValid("((("))
print(minAddToMakeValid("("))