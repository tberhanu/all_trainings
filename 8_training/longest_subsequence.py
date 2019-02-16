"""
This is dynamic programming used to solve the problem.
"""
def longest_subsequence(arr):
    longest = [1]*len(arr)
    i, j = 0, 1
    while j < len(arr):
        if arr[j] > arr[i]:
            longest[j] = max(longest[j], 1 + longest[i])

        i = i + 1
        if i == j:
            i = 0
            j = j + 1
    return max(longest)


print(longest_subsequence([3, 4, -1, 0, 6, 2, 3]))
#4
print(longest_subsequence([2, 5, 1, 8, 3]))
#3
