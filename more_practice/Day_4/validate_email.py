""" QUESTION 6 """

def is_valid(email):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z.-]+$')
    match = pattern.match(email)
    return bool(match)


print(is_valid("CoreyMSchafer@gmail.com"))
print(is_valid("corey.schafer@university.edu"))
print(is_valid("corey-321-schafer@my-work.net"))
print(is_valid("CoreyMSchafer@@gmail.com"))
print(is_valid("CoreyMSchafer@gmail.com_edu"))

