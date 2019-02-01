"""
https://www.hackerrank.com/challenges/compress-the-string/problem

Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character 1 occurs only once. It is replaced by (1, 1). Then the character 2 occurs
 three times, and it is replaced by (3, 2) and so on.

Also, note the single space within each compression and between the compressions.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

string = input()
cntr = 1
arr = []
for i, s in enumerate(string):
    if i + 1 < len(string) and string[i] != string[i+1]:
        tup = (cntr, s)
        arr.append(tup)
        cntr = 0
    if i + 1 == len(string):
        tup = (cntr, s)
        arr.append(tup)
    else:
        cntr = cntr + 1
        
print(" ".join(("("+str(a[0])+", "+str(a[1]) + ")") for a in arr))
