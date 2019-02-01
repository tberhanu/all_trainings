"""
https://www.hackerrank.com/challenges/re-start-re-end/problem?h_r=next-challenge&h_v=zen
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s, k = input(), input()
i = 0
found = False
while i < len(s):
    string = s[i:]
    match = re.match(r'{}'.format(k), string)
    if match == None:
        i = i + 1
    else:
        found = True
        print((match.start() + i, match.end() + i - 1))
        i = i + 1

if not found:
    print('(-1, -1')