def foo(m, n):
    sum = 0
    cntr = 0
    while sum <= m:
        sum = sum + n
        if sum <= m:
            cntr = cntr + 1
    return cntr



print(foo(34, 3))

print(foo(7, 3))
print(foo(6, 2))

