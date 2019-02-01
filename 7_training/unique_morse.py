""" https://leetcode.com/problems/unique-morse-code-words/
804. Unique Morse Code Words

"""
def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    values = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    d = dict(zip(keys, values))
    from collections import Counter
    arr = []
    for w in words:
        decoded = ""
        for char in w:
            decoded = decoded + d[char]
        arr.append(decoded)
    counter = dict(Counter(arr))
    return len(counter)