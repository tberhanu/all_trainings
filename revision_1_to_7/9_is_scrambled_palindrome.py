"""
9. Return True if the str is a scrambled palindrome
Ex. arceace --> is True b/c acereca is a palindrome
"""
from collections import Counter

def is_scrambled_palindrome(string):

    counter = Counter(string)
    odds = sum(1 for c in counter.values() if c % 2 != 0)
    if len(string) % 2 == 0:
        return odds == 0
    else:
        return odds == 1





print(is_scrambled_palindrome("arceace"))
print(is_scrambled_palindrome("kabbak"))
print(is_scrambled_palindrome("bbab"))