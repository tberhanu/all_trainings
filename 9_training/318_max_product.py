"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain
only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


def maxProduct(words):
    """Runtime: 3416 ms, faster than 8.86% of Python3 online submissions for Maximum Product of Word Lengths.

    CAN YOU MAKE IT BETTER ?????
"""
    ordered = sorted(words, key=lambda a: len(a), reverse=True)
    i = 0
    largest = 0
    while i < len(ordered):
        j = i + 1
        while j < len(ordered):
            a = ordered[i]
            b = ordered[j]
            if set(a) & set(b):
                j = j + 1
                continue
            else:
                p = len(a) * len(b)
                if p > largest:
                    largest = p
                break

        i = i + 1
    return largest



print(maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
# print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))