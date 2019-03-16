"""https://www.hackerrank.com/challenges/picking-numbers/problem?h_r=next-challenge&h_v=zen&isFullScreen=false"""

def pickingNumbers(a):

    a.sort()
    i, j, cntr, big = 0, 0, 0, 0
    while j < len(a):
        if abs(a[i] - a[j]) <= 1:
            cntr += 1
        else:
            if cntr > big:
                big = cntr
            cntr = 0
            i = j
            j -= 1
        j += 1

    return max(big, cntr)

a = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(a))
a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(pickingNumbers(a))





