"""
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""

import re


def fun(s):

    # return True if s is a valid email, else return False
    pattern = re.compile(r'^[a-zA-Z0-9_-]+@[0-9a-zA-Z]+\.[a-zA-Z]{1,3}$')
    return bool(pattern.match(s))


def filter_mail(emails):

    return list(filter(fun, emails))


if __name__ == '__main__':

    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)