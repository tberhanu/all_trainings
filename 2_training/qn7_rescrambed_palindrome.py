#!/usr/bin/env python3
from collections import Counter

def is_palindrome(str):
    """is_palindrome(str) --> a function taking a string and output a boolean telling if that string is a scrambled
    palindrome or not.

    :param str: String
    :return: Boolean
    """
    counter = Counter(list(str))
    # print(counter)
    cntr = 0
    for key in counter:
        if counter[key] % 2 != 0:
            cntr += 1
            if len(str) % 2 == 0 and cntr > 0:
                return False
            elif len(str) % 2 != 0 and cntr > 1:
                return False

    return True

if __name__ == "__main__":
    print(is_palindrome("arca"))
    print(is_palindrome("arceace"))

