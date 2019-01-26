""" 318. Maximum Product of Word Lengths
    Given a string array words, find the maximum value of length(word[i]) * length(word[j])
    where the two words do not share common letters. You may assume that each word will contain
    only lower case letters. If no such two words exist, return 0."""

def maxProduct(words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = []
        for i, w in enumerate(words):
            for j, ww in enumerate(words, i + 1):
                if not set(w) & set(ww):
                    result.append(len(w) * len(ww))

        return 0 if len(result) == 0 else max(result)

arr = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(maxProduct(arr))
arr = ["a","ab","abc","d","cd","bcd","abcd"]
print(maxProduct(arr))
arr = ["a","aa","aaa","aaaa"]
print(maxProduct(arr))
