
def palindrome(string):
    i = 0
    j = len(string)

    while i < j:
        biggest = string[i:j]
        if biggest == biggest[::-1]:
            return biggest
        bigger1 = string[i + 1:j]
        bigger2 = string[i:j - 1]
        if bigger1 == bigger1[::-1]:
            return bigger1
        if bigger2 == bigger2[::-1]:
            return bigger2
        i = i + 1
        j = j - 1

# print(palindrome("babad"))
# print(palindrome("cbbd"))
# print(palindrome("dbabbabcd"))

print(palindrome("babad"))
print("----")
print(palindrome("cbbd"))
print("----")
print(palindrome("dbabbabcd"))
