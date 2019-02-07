"""Question 1
Perform addition using decorators (Here in the Decorator function
make sure that numbers are valid)
"""


def decorator_func(original_func):

    def wrapper_func(*args, **kwargs):

        if (type(args[0]) is int or type(args[0]) is float) and (type(args[1]) is int or type(args[1]) is float):
            return original_func(*args, **kwargs)
        else:
            return "Not valid numbers"

    return wrapper_func

@decorator_func
def addition_func(a, b):
    return "{} + {} = {}".format(a, b, a + b)


print(addition_func("999", 1000))
print(addition_func("hello", 8))
print(addition_func(999, 1000))