def gcd(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return temp

def gcd2(x, y):
    while x != y:
        if x > y:
            x = x - y
        if y > x:
            y = y - x
    return x
import time
start1 = time.time()
print(gcd(150, 200))
print(gcd(1588, 258))
print(gcd(211, 144))
print(gcd(33, 77))
a = time.time() - start1
print(a)
print("---------")
start2 = time.time()
print(gcd2(150, 200))
print(gcd2(1588, 258))
print(gcd2(211, 144))
print(gcd2(33, 77))
b = time.time() - start2
print(b)
if a - b > 0:
    print("gcd2 is faster than gcd")
if a - b < 0:
    print("gcd is faster than gcd2")
print(a - b)

