# https://www.hackerrank.com/contests/projecteuler/challenges/euler004
def largest_palindrome(N):
    largest = 101101
    for i in range(999, 99, -1):
        k = min(i, (N // i))
        for j in range(k, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1]and product < N :
                if product > largest:
                    largest = product
    return largest

def largest_palindrome2(N):
    largest = 101101
    for i in range(999, 99, -1):
        # k = min(i, (N // i) + 1)
        for j in range(999, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1]and product < N :
                if product > largest:
                    largest = product
    return largest
if __name__ == '__main__':
    import time
    start = time.time()
    print(largest_palindrome(1000000))
    print(time.time() - start)
    start = time.time()
    print(largest_palindrome2(1000000))
    print(time.time() - start)
