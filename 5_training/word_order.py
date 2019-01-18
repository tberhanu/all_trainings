# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
from collections import Counter
arr = []
for line in fileinput.input():
    arr.append((line).rstrip())
n = arr[0].split()
words = []
for i in range(int(n[0])):
    words.append(arr[i + 1])
counter = Counter(words)
print(len(counter))
s = ""
sets = set()
for a in words:
    if a not in sets:
        s = s + str(counter[a]) + " "
    sets.add(a)
print(s)