"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(n):
    dict = {1: 1, 2: 2, 3: 3}
    return foo(n, dict)

def foo(n, dict):
    if n in dict:
        return dict[n]
    if n < 0:
        return 0
    if n == 0:
        return 1

    dict[n] = climbStairs(n - 2) + climbStairs(n - 1)
    return dict[n]

# print(climbStairs(38))
print(climbStairs(1)) #1
print(climbStairs(2)) #2
print(climbStairs(3)) #3
print(climbStairs(4)) #5
