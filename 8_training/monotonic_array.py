"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

"""


def isMonotonic(A):
    """Runtime: 64 ms, faster than 90.07% of Python online submissions for Monotonic Array.
"""
    status = 0
    set = True
    for i in range(1, len(A)):
        diff = A[i] - A[i-1]
        if diff == 0:
            continue
        elif status == 0 and set:
            status = 1 if diff > 0 else -1
            set = False
        if (diff > 0 and status < 0) or (diff < 0 and status > 0):
            return False
    return True


print(isMonotonic([3,4,2,3]))
print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))
print(isMonotonic([1,2,4,5]))
print(isMonotonic([1,1,1]))
