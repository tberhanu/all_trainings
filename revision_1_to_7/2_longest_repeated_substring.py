"""
2. Given a str, what is the longest substring with repeated or same characters.
If found 2 or more, use alphabetical order
"""

from collections import Counter, OrderedDict

class CounterOrderedDict(Counter, OrderedDict):

    pass

def longest_repeated_substring(string):

    myobj = CounterOrderedDict(sorted(string))
    return myobj.most_common(1)[0][0]


print(longest_repeated_substring("bbccaadd"))