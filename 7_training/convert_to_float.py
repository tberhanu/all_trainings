"""
Get the most repeated char of the given string. If two chars occur same number of times,
return in alphabetical order.
"""
# from collections import Counter, OrderedDict
#
#
# class CounterOrderedDict(Counter, OrderedDict):
#
#     pass
#
#
# def foo(string):
#     esp_cntr = CounterOrderedDict(sorted(string))
#
#     return esp_cntr.most_common(1)[0][0]
#
# s = "zzzzzbbbbcccaaa"
# print(foo(s))

import re
def convert_to_float(s):
    match = re.match(r'[-+][0-9]+\.[0-9]+', s)
    print(round(float(match.group()), 2))

convert_to_float("-7.934here")
convert_to_float(("+9.455"))