"""
1. Given a str, what is the longest palindrome
"""

def longest_palindrome(string):
    i = 0
    pal = string[0]
    while i < len(string):
        j = i + 2
        while j <= len(string):
            if string[i:j] == string[i:j][::-1]:
                if len(string[i:j]) > len(pal):
                    pal = string[i:j]
            j = j + 1
        i = i + 1
    return pal


import numpy as np

def longestPalindrome(str):
    """
    :type s: str
    :rtype: str
    """

    n = len(str)
    # pal = [][]
    start_index = 0
    max_length = 1
    pal = np.zeros([n, n])
    if str == str[::-1]:
        return str
    for i in range(n):
        pal[i][i] = True
    for i in range(n - 1):
        if str[i] == str[i + 1]:
            pal[i][i + 1] = True
            start_index = i
            max_length = 2
        else:
            pal[i][i + 1] = False
    curr = 3
    while curr <= n:
        i = 0
        while i < n - curr + 1:
            j = i + curr - 1
            if str[i] == str[j] and pal[i + 1][j - 1]:
                pal[i][j] = True
                if max_length < curr:
                    max_length = curr
                    start_index = i
            else:
                pal[i][j] = False
            i = i + 1
        curr = curr + 1

    return str[start_index: start_index + max_length]


print(longest_palindrome('eabcb'))

print(longest_palindrome("babad"))
print(longestPalindrome("eabcb"))
print(longestPalindrome("babad"))

print(longest_palindrome("b"))
print(longest_palindrome("baabaabk"))
print(longest_palindrome("baab"))
print(longest_palindrome("abcdefg"))
