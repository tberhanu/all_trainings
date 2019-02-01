"""
https://www.hackerrank.com/challenges/re-group-groups/problem?h_r=next-challenge&h_v=zen
You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right)
that has consecutive repetitions.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re
pattern = re.compile(r'([a-zA-Z0-9])(?=\1)')
for line in sys.stdin:
    matches = pattern.findall(line)
    if len(matches) > 0:
        print(matches[0])
    else:
        print('-1')
