""" https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?h_r=next-challenge&h_v=zen
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re
pattern = re.compile(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', re.I)
for line in sys.stdin:
    matches = pattern.findall(line)
    if len(matches):
        for match in matches:
            print(match)
    else:
        print(-1)
