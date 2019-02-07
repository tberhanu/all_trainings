""" QUESTION 4 """
def is_palindrome(string):
    return string == string[::-1]



string = "carrac"
print(is_palindrome(string))
string = "acrrcaa"
print(is_palindrome(string))