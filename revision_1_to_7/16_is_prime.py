"""
16. Check efficiently if the given number is a prime or not
"""
import math
import time


def is_prime_v1(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_v2(num):
    if num <= 1:
        return False
    for i in range(2, 1 + math.floor(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


def is_prime_v3(num):
    if num == 2:
        return True
    if num <= 1 or (num > 2 and num % 2 == 0):
        return False
    for i in range(3, 1 + math.floor(math.sqrt(num)), 2):
        if num % i == 0:
            return False
    return True


start1 = time.time()
for i in range(10000):
    if is_prime_v1(i):
        print(i, is_prime_v1(i))
end1 = time.time()
interval1 = end1 - start1

start2 = time.time()
for i in range(10000):
    if is_prime_v2(i):
        print(i, is_prime_v1(i))
end2 = time.time()
interval2 = end2 - start2

start3 = time.time()
for i in range(10000):
    if is_prime_v3(i):
        print(i, is_prime_v1(i))
end3 = time.time()
interval3 = end3 - start3

print("Version One time: {}".format(interval1))
print("Version Two time: {}".format(interval2))
print("Version Three time: {}".format(interval3))
