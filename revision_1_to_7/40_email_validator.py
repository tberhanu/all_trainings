"""
Given 1) an array of emails like emails = ["tess@gmail.com", "kkk%gmail.com"]
      2) def filter_email(emails):
            return list(filter(email_validator, emails))
Write the function email_validator that receives a string and validate whether it's a valid
email or not.
"""
def filter_email(emails):
    return list(filter(email_validator, emails))

def email_validator(string):
    import re
    pattern = re.compile(r'[\w_-]+@[\w_-]+\.[a-zA-Z]{1,3}$')
    match = pattern.match(string)
    return bool(match)

emails = ["tess@gmail.com", "kkk%gmail.com", "berhanu@@gmail.com", "test@yahoo@.com", "hello@a.c"]
print(filter_email(emails))