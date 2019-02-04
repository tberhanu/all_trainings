"""
Get the second largest/smallest element of the arr
"""
def nth_largest_smallest(arr, n):
    import heapq
    nth_largest = heapq.nlargest(n, arr)
    nth_smallest = heapq.nsmallest(n, arr)
    return nth_largest, nth_smallest



print(nth_largest_smallest([1, 4, 45, 33, 4, 33, 45, 1, 4], 2))