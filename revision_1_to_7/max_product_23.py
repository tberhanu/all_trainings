"""
23. Given an array of strings, words = ["...", "...", "...."], find maximum value of
len(words[i]) * len(words[j]) where the two words don't share common letter/letters.
If no two words exist return 0.
"""

def max_product(arr):

    result = max([0] + [len(a) * len(b) for a in arr for b in arr if len(set(a) & set(b)) == 0])
    return result

