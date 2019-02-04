"""
26. A wiggle sequence is if the difference b/n successive numbers strictly alternate between +ve
and -ve. Given a sequence of ints, return the length of the longest subsequence that is a
wiggle sequence. Assumption is the first status is either +ve or -ve, but not 0

Ex. [1, 7, 4, 9, 2, 5] --> 6
Ex. [1, 17, 5, 10, 13, 15, 10, 5, 16, 8] --> 7 b/c [1, 17, 10, 13, 10, 16, 8] is one of those
Ex. [1, 2, 3, 4, 5, 6, 7, 8, 9] --> 2
"""

def longest_subsequence(arr):

    i = 0
    j = i + 1
    cntr = 1
    status = get_status(arr[1], arr[0])
    while j < len(arr):
        status2 = get_status(arr[i], arr[j])
        if status2 != 0 and status2 != status:
            cntr = cntr + 1
            status = status2
            i = i + 1
            j = j + 1
        else:
            j = j + 1
    return cntr


def get_status(e1, e2):
    if e2 == e1:
        return 0
    elif e2 > e1:
        return 1
    else:
        return -1




print(longest_subsequence([1, 7, 4, 9, 2, 5]))
#6
print(longest_subsequence([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
#7
print(longest_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#2