""" QUESTION 7
Write a program that validates if the given phone number is valid
(Assume +1 234 567 2345 and 234 567 2345 both are valid)
"""
def is_valid(phone):
    import re
    pattern = re.compile(r'^(\+1\s)?[0-9]{3}\s[0-9]{3}\s[0-9]{4}$')
    match = pattern.match(phone)
    return bool(match)


print(is_valid("+1 234 567 2345"))
print(is_valid("234 567 2345"))
print(is_valid("1234 567 2345"))
print(is_valid("1 234 567 2345"))