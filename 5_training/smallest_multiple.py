def smallest_multiple(N):
    n = N if N % 2 == 0 else N + 1
    flag = True
    while True:
        for i in range(2, N + 1):
            if n % i != 0:
                flag = False
                break
        if flag:
            return n
        else:
            flag = True
        n = n + 2

print(smallest_multiple(10))
print(smallest_multiple(11))
