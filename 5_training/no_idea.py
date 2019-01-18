# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
arr = []
for line in fileinput.input():
    arr.append(line)
n, m = arr[0].split()
arr2 = arr[1].split()
A = set(arr[2].split())
B = set(arr[3].split())
h = 0
for a in arr2:
    if a in A:
        h = h + 1
    if a in B:
        h = h - 1
print(h)


