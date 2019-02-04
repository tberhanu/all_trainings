""" 921. Minimum Add to Make Parentheses Valid
    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""
def minAddToMakeValid(string):
    """
    :type string: str
    :rtype: int
    """
    open, close, cntr = 0, 0, 0
    lst = list(string)
    i = 0
    while i < len(lst):
        if lst[i] == ")" and open > 0:
            del lst[i]
            del lst[i - 1]
            open -= 1
            i -= 1

        elif lst[i] == "(":
            open += 1
            i = i + 1
        else:
            if lst[i] == ")" and open == 0:
                cntr += 1
                i = i + 1
    return open + cntr

string = "())"
print(minAddToMakeValid(string))
string = "((("
print(minAddToMakeValid(string))
string = "()"
print(minAddToMakeValid(string))
string = "()))(("
print(minAddToMakeValid(string))
