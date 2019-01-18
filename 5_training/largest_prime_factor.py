#
# import math
#
# def largest_prime_factor(N):
#     if N % 2 == 0:
#         return even_func(N)
#     else:
#         return odd_func(N)
# def even_func(N):
#
#     while N >= 2:
#         n = N // 2
#         if is_prime(n):
#             return n
#         N = N // 2
#
# def odd_func(N):
#
#     i = 3
#     prime = 0
#     while(i <= math.sqrt(N)):
#         if N % i != 0:
#             i = i + 2
#         else:
#             if is_prime(i):
#                 prime = i
#                 N = N // i
#                 i = 3
#     return prime
#
# def is_prime(N):
#     if N == 2:
#         return True
#     elif N % 2 == 0:
#         return False
#     else:
#         i = 3
#         while(i <= math.sqrt(N)):
#             if N % i == 0:
#                 return False
#             i = i + 1
#         return True
# print(largest_prime_factor(13195))
# print(largest_prime_factor(17))
#
# print(is_prime(21))
#
#

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        while n%i == 0:
            n = n // i
        i = i + 1

    return max(2, n)

# print(largest_prime_factor(13195))

