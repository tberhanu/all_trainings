"""
28. Given a str or arr, get the N most common(repeated) chars. If two have same
frequency, use alphabetical order.
"""
from collections import Counter, OrderedDict
class CounterOrderedDict(Counter, OrderedDict):
    pass
def most_common_chars(string, n):
    string = string.replace(" ", "")
    esp_counter = CounterOrderedDict(string)
    return esp_counter.most_common(n)


string = """Given a str or arr, get the N most common(repeated) chars. If two have same
frequency, use alphabetical order."""
print(most_common_chars(string, 3))
