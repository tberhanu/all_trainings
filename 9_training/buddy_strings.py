"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two
letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
def is_buddy_strings(A, B):
    """Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Buddy Strings.
"""
    if len(A) != len(B):
        return False
    if len(A) <= 1:
        return False
    if A == B and len(A) != len(set(A)):
        return True
    a, b = list(A), list(B)
    cntr = 0
    indexes = []
    for i in range(len(a)):
        if a[i] != b[i]:
            cntr = cntr + 1
            indexes.append(i)
            if cntr > 2:
                break

    if cntr != 2:
        return False
    i, j = indexes[0], indexes[1]
    a[i], a[j] = a[j], a[i]
    return a == b

# def is_buddy_strings(A, B):
# """Runtime: 96 ms, faster than 6.53% of Python3 online submissions for Buddy Strings.
#     CAN YOU MAKE IT BETTER?????
# """
#     if len(A) != len(B):
#         return False
#     if len(A) <= 1:
#         return False
#     if len(A) >= 2 and A == B and len(set(A)) != len(A):
#         return True
#     i, j = 0, len(A) - 1
#     a = list(A)
#     b = list(B)
#     while i <= j and i < len(a) and j < len(b):
#         if a[i] == b[i]:
#             del a[i]
#             del b[i]
#             j = j - 1
#         else:
#             i = i + 1
#         if a[j] == b[j]:
#             del a[j]
#             del b[j]
#             j = j - 1
#         else:
#             j = j - 1
#     return len(a) == 2 and a == b[::-1]
#



A = "aaaaaaabc"
B = "aaaaaaacb"
print(is_buddy_strings(A, B)) # True
A = "aa"
B = "aa"
print(is_buddy_strings(A, B)) # True
A = ""
B = "aa"
print(is_buddy_strings(A, B)) # False
A = "ab"
B = "ba"
print(is_buddy_strings(A, B)) # True
A = "abcaa"
B = "abcbb"
print(is_buddy_strings(A, B)) # False

A = "abab"
B = "abab"
print(is_buddy_strings(A, B)) # True
