"""
30. Given a str, find the first occurrence of alphanumeric that has consecutive repetition
Ex. "..!!abcd22efe22fff" --> "2", not "." since it's not alphanumeric
"""
import re
def first_consecutive(string):

    pattern = re.compile(r'([\w])(?=\1)')
    match = pattern.search(string)
    return match.group()


print(first_consecutive("..!!abcd22efe22fff"))