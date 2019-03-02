"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character but a character may map
to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

def is_isomorphic(s, t):
    """Runtime: 48 ms, faster than 63.56% of Python3 online submissions for Isomorphic Strings.

    This problem is indirectly involving a dictionary with not only unique keys but also
    unique values, as we can't map same value for two different letters.
"""
    dict1 = {}
    dict2 = {}

    for i, j in zip(s, t):
        if i not in dict1:
            dict1[i] = j
        else:
            if dict1[i] != j:
                return False
        if j not in dict2:
            dict2[j] = i
        else:
            if dict2[j] != i:
                return False
    return True

print(is_isomorphic("paper", "title"))
print(is_isomorphic("papere", "titlee"))
