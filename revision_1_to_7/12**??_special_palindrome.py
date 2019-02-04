"""
12. Given a string, return how many special palindromes(where all characters
are same except the middle one)
Ex. aaa, aadaa but not dggd
"""
""" This code works but TOO SLOW to run within the expected time interval"""
def special_palindromes_count(string):

    letters = 2
    counter = 0
    arr = []
    while letters <= len(string):
        start = 0

        while start + letters <= len(string):
            s = string[start: start + letters]
            if len(s) % 2 == 0 and s.count(s[0]) == len(s):
                arr.append(s)
                counter += 1
            elif is_esp_pal(s):
                arr.append(s)
                counter += 1
            start += 1
        letters += 1
    print(arr)
    return len(arr) + len(string)



def is_esp_pal(string):

    if string.count(string[0]) == len(string):
        return True
    mid = len(string) // 2
    lefty = string[:mid]
    righty = string[mid+1:]
    return lefty.count(lefty[0]) == len(lefty) and lefty == righty



print(special_palindromes_count("aaa"))
print(special_palindromes_count("aadaa"))
print(special_palindromes_count("dggd"))
print(special_palindromes_count("mnonopoo"))
print(special_palindromes_count("abcbaba"))