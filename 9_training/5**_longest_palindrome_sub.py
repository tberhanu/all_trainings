"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def longestPalindrome(s):
    """Runtime: 5044 ms, faster than 19.81% of Python3 online submissions for Longest Palindromic Substring.

    CAN YOU MAKE IT BETTER ??????
"""
    i, j = 0, len(s)
    longest = 1
    while i < len(s):
        j = len(s)
        while j >= 0:
            slice = s[i:j]
            if len(slice) <= longest:
                break
            if slice == slice[::-1] and len(slice) > longest:
                longest = len(slice)
                break
            j = j - 1
        i = i + 1
    return longest


