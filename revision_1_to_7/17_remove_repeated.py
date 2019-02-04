"""
17. Given a string and num k, split the string in len(string) / k, and from a split sections
remove the repeated occurrences
Ex. str = "aabcaaada", k = 3 ---> ab ca ad
"""

def remove_repeated_occurrences(string, k):
    arr = []
    step = len(string)//k if len(string) % k == 0 else (len(string) // k ) + 1
    for i in range(0, len(string), step):
        s = string[i:i+step]
        ss = remove_repetition(s)
        arr.append(ss)

    return arr


def remove_repetition(string):
    lst = list(string)
    i = 0
    while i < len(string):
        if i + 1 < len(lst) and lst[i] == lst[i + 1]:
            del lst[i]
        else:
            i = i + 1
    return "".join(lst)



print(remove_repeated_occurrences("aabcaaada", 3))
print(remove_repeated_occurrences("aabcaaada", 2))