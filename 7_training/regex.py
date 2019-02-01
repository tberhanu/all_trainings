#!/usr/bin/env python3

import re
# emails = '''
# Here is the @ emails:
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# @ofcourse the end is here
# '''
#
#
# pattern = re.compile(r'[0-9a-zA-Z\.-]+@[a-zA-Z\.-]+\.[a-zA-Z]+')
#
# matches = pattern.findall(emails)
# for match in matches:
#     print(match)

string = "Todays is 2012-11-27 but ofcourse 2013-12-23 done"
s = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', string)
print(s)

text = "STart and End"
pattern = re.compile(r'(^S)(End$)')
matches = pattern.findall(text)
for m in matches:
    print(m)
