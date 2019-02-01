text = "4.5 5.5 -0.7 +7.7 4 5 4555 .9 .99"

import re

pattern = re.compile(r'[+-]?[0-9]*\.[0-9]+')

matches = pattern.findall(text)

for match in matches:
    print(match)

