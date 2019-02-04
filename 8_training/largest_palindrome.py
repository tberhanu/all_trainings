# def palindrome(string):
#     i, j = 0, len(string)
#     while i < j:
#         if is_pal(string[i:j]):
#             return string[i:j]
#         if is_pal(string[i+1:j]):
#             return string[i+1:j]
#         if is_pal(string[i:j-1]):
#             return string[i:j-1]
#         i = i + 1
#         j = j - 1
def palindrome(string):
    save = ""

    for i in range(len(string)):

        for j in range(len(string), -1, -1):

            str = string[i:j]
            if str == str[::-1] and len(str) > len(save):
                save = str
                break
        next = string[i+1:]
        if len(save) >= len(next):
            print(save)
def is_pal(str):

    return str == str[::-1]

# print(palindrome("babad"))
# print(palindrome("cbbd"))
# print(palindrome("dbabbabcd"))

palindrome("babad")
print("----")
palindrome("cbbd")
print("----")
palindrome("dbabbabcd")
