"""
24. Given a string, return the reversed string where all the characters
 that aren't a letter stay in the same place.
 Ex. "ab-cd#ef" --> "fe-dc#ba"
 Ex. "a-bC-dEf-ghIj" --> "j-Ih-gfE-dCba"
"""
def reverse_string(string):
    letters = "abcdefghijk"
    letters = letters + letters.upper()
    i = 0
    j = len(string) - 1
    string = list(string)
    while i < j:
        if string[i] in letters and string[j] in letters:
            string[i], string[j] = string[j], string[i]
            i = i + 1
            j = j - 1
        if string[i] not in letters:
            i = i + 1
        if string[j] not in letters:
            j = j - 1
    return "".join(string)



print(reverse_string("ab-cd#ef"))
print(reverse_string("a-bC-dEf-ghIj"))