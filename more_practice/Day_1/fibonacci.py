""" 2. Write a program to find Fibonacci sequence

"""
def fibonacci(n):
    dict = {0: 0, 1: 1}
    def fib(n, dict):
        if n in dict:
            return dict[n]
        else:
            result = fib(n - 1, dict) + fib(n - 2, dict)
            dict[n] = result
            return result
    return fib(n, dict)


for i in range(11):
    print(i, fibonacci(i))