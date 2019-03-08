

# def foo(N):
#     import math
#     print(math.log2(N))
#
#
# foo(256)

def is_power_of_two(x):
    return (x != 0) & ((x & (x - 1)) == 0)


print(is_power_of_two(256))
print(is_power_of_two(32))
print(is_power_of_two(0))
print(is_power_of_two(24))

def is_opposite_signs(x, y):
    return (x ^ y) < 0
def is_same_sign(x, y):
    return (x ^ y) > 0
print("---------------------")
print(is_opposite_signs(2, 3))
print(is_opposite_signs(2, -3))
print(is_opposite_signs(-3, 9))
print(is_opposite_signs(0, 9))
print(is_opposite_signs(0, -9))

