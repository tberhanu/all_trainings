"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

def is_valid_palindrome(statement):
    """Runtime: 52 ms, faster than 98.15% of Python3 online submissions for Valid Palindrome.
"""
    import re
    pattern = re.compile(r'\w+', re.I)
    matches = pattern.findall(statement)
    string = "".join(matches).lower()
    return string == string[::-1]








print(is_valid_palindrome("A man, a plan, a canal: Panama"))
print(is_valid_palindrome("race a car"))
