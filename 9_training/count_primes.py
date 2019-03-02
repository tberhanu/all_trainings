"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

def count_primes(n):
    if n <= 2:
        return 0
    primes = [1] * n
    primes[0] = 0
    primes[1] = 0
    i = 2
    while i * i <= n:
        if primes[i]:
            j = 2
        while i * j < n:
            primes[i * j] = 0
            j = j + 1
        i = i + 1
    return sum(primes)

print(count_primes(10))
print(count_primes(3))
print(count_primes(9))
