"""396. Rotate Function

https://leetcode.com/problems/rotate-function/

My code works for almost all the tests but failed to finish within the expected
time interval of the leetcode question maker but here is the help.
Here is the mathematics concept behind this solution I learned from the discussion

  f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
  f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k]
=>f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +       A[k-1]    - k * A[k]
   = (A[0]   +   A[1]   +   A[2] + ...  +       A[k-1] + k * A[k]) - (k+1) * A[k]
   = sum(Array) - A[k] * array.length
=> f(i+1) = f(i) + sum(Array) -  last element * array.length

"""
def max_rotate_function(A):
    highest = curr = sum(i * j for i, j in enumerate(A))
    normal_array_sum = sum(A)
    normal_array_length = len(A)
    while A:
        curr += normal_array_sum - A.pop() * normal_array_length
        highest = max(curr, highest)
    return highest

A = [4, 3, 2, 6]
print(max_rotate_function(A))
