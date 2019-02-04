text = "Today is 11-12-2019 and 55-53-8888 ofcourse"

import re

pattern = re.compile(r'(\d+)-(\d+)-(\d+)')

matches = pattern.findall(text)
print(matches)

matches = pattern.finditer(text)
for match in matches:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print("---")

print("*************** without grouping ********** ")
pattern = re.compile(r'\d+-\d+-\d+')

matches = pattern.findall(text)
print(matches)

matches = pattern.finditer(text)
for match in matches:
    print(match.group())
    # print(match.group(1))
    # print(match.group(2))
    # print(match.group(3))
    print("---")