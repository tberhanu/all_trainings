"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
def length_of_last_word(s):
    if s == "" or s.isspace():
        return 0
    return len(s.split()[-1])


print(length_of_last_word("Hello World"))
print(length_of_last_word(""))
print(length_of_last_word(" "))
print(length_of_last_word("          "))
