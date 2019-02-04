"""
29. Compress string like 1222311 --> (1, 1) (3, 2) (1, 3) (2, 1) using a pattern of (freq, num)
"""
def compress(string):

    i = 1
    cntr = 1
    arr = []
    while i < len(string):
        if string[i] == string[i-1]:
            cntr = cntr + 1
        else:
            arr.append((cntr, string[i-1]))
            cntr = 1
        i = i + 1
    arr.append((cntr, string[i - 1]))
    return arr


print(compress("1222311"))