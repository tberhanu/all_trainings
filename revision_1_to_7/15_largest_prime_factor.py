"""
15. Given an int, what is the largest prime factor?
"""

def largest_prime_factor(num):

    i = 2
    while i * i <= num:
        while num % i == 0:
            num = num // i
        i = i + 1

    return max(2, num)


print(largest_prime_factor(12))
print(largest_prime_factor(15))
print(largest_prime_factor(21))
print(largest_prime_factor(16))




