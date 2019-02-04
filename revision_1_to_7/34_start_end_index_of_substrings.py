"""
34. Given a string S and Substing s, get all the matched s in S as start and end index.
Solve this problem using i) Regex ii) Other ways
Ex. S = "aaadaa", s = "aa" --> (0, 1) (1, 2) (4, 5)
"""
def start_end_index(string, s):
    size = len(s)
    arr = []
    for i in range(len(string)):
        if s == string[i:i + size]:
            arr.append((i, i + size-1))
    return arr








print(start_end_index("aaadaa", "aa"))