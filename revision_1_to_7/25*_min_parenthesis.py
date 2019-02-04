"""
25. Given an incomplete parenthesis, what is the minimum parenthesis to make
a valid or complete parenthesis.
Ex. ()) --> 1, () --> 0, ((( --> 3, ()))(( --> 4
"""

def min_parenthesis(string):

    cntr = 0
    i = 0
    string = list(string)
    while string:
        if string[i] == ")" and i == 0:
            cntr += 1
            del string[i]
        elif string[i] == "(" and i == len(string) - 1:
            cntr += 1
            del string[i]
            i = i - 1
        elif i - 1 >= 0 and string[i-1] == "(" and string[i] == ")":
            del string[i-1:i+1]
            i = i - 1

        else:
            i = i + 1


    return cntr



print(min_parenthesis("())"))
print(min_parenthesis("()"))
print(min_parenthesis("()))(("))