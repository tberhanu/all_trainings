"""
https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
"""
def superDigit(n, k):
    summed = sum(int(num) for num in n)
    summed = summed * k
    return foo(summed)

def foo(summed):
    if summed < 10:
        return summed

    summed = sum(int(num) for num in str(summed))
    return foo(summed)



print(superDigit("123", 3))