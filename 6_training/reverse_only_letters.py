""" Given a string S, return the "reversed" string where all characters that
are not a letter stay in the same place, and all letters reverse their positions.
"""
def reverseOnlyLetters(S):
        """
        :type S: str
        :rtype: str
        """
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        arr = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            if arr[i] not in letters:
                i = i + 1
            if arr[j] not in letters:
                j = j - 1
            if arr[i] in letters and arr[j] in letters:
                arr[i], arr[j] = arr[j], arr[i]
                i = i + 1
                j = j - 1
        return "".join(arr)
