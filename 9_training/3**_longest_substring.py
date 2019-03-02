"""Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s):
    """Your runtime beats 10.70 % of python3 submissions.

    CAN YOU MAKE IT BETTER       ??????
"""
    arr = [1] * len(s)
    i = 0
    j = 1
    while j < len(s):
        if s[j] not in s[i:j]:
            arr[i] += 1
            j = j + 1
        else:
            i = i + 1
            j = i + 1
    return max(arr)

def lengthLongestSubstring_two(string):
    if len(string) == 0:
        return 0
    arr = [1] * len(string)
    i = 0
    j = 1
    sets = set(string[0])
    while j < len(string):
        if string[j] not in sets:
            sets.add(string[j])
            arr[i] += 1
            j = j + 1
        else:

            i = i + 1
            sets = {string[i]}
            j = i + 1
    return max(arr)


print(lengthOfLongestSubstring("pwwkew"))