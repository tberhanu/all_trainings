arr = [2, 3, 6, 6, 5]
largest = max(arr)
m = max(a for a in arr if a != largest)
print(m)