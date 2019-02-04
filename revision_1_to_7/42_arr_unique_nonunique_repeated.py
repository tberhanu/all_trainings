"""
Given an arr: i) Get uniques
              ii) Get non uniques
              iii) Get non uniques from sorted arr
              iv) Get the first repeated element
"""
def get_uniques(string):
    from collections import Counter
    freq = Counter(string)
    return [k for k, v in freq.items() if v == 1]
def get_unique_set(string):
    dict = {}
    return [dict.setdefault(c, c) for c in string if c not in dict]
def get_unique_set_two(string):
    return list(set(string))
def get_non_uniques(string):
    from collections import Counter
    freq = Counter(string)
    return [k for k, v in freq.items() if v != 1]

# def get_non_uniques_from_sorted_arr(arr):
# def get_first_repeated(string):
#     import re
#     pattern = re.compile(r'(.)\1')
#     match = pattern.findall(string)
#     return match[0]

print(get_uniques("abcdacdz"))
print(get_unique_set("abcdacdz"))
print(get_unique_set_two("abcdacdz"))
print(get_non_uniques("abcdacdz"))
print(get_first_repeated("aabbcdbbaacdz"))