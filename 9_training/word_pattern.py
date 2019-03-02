"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters
separated by a single space.
"""

def word_pattern(pattern, str):
    """Your runtime beats 17.13 % of python3 submissions.
"""
    lst = str.split()
    if len(pattern) != len(lst):
        return False
    zipped = zip(pattern, lst)
    dict = {}
    for tup in zipped:
        if tup[0] not in dict and tup[1] in dict.values():
            return False
        if tup[0] not in dict:
            dict[tup[0]] = tup[1]
        if tup[0] in dict and dict[tup[0]] != tup[1]:
            return False

    return True

def smart_way(pattern, str):
    """Runtime: 48 ms, faster than 22.07% of Python3 online submissions for Word Pattern.
"""
    lst = str.split()
    if len(pattern) != len(lst):
        return False
    zipped = zip(pattern, lst)
    return len(set(pattern)) == len(set(lst)) == len(set(zipped))


str = "dog dog dog dog"
print(word_pattern("abba", str))
str = "dog cat cat dog"
print(word_pattern("abba", str))
str = "dog cat cat dog"
print(word_pattern("aaaa", str))
