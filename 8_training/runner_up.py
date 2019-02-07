
def runner_up(arr):
    largest = max(arr)
    return max(a for a in arr if a != largest)

def runner_up2(arr):
    import heapq
    return heapq.nlargest(2, set(arr))[1]


arr = [2, 3, 6, 6, 5]
print(runner_up(arr))
print(runner_up2(arr))