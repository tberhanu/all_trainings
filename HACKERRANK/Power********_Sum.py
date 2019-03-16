











"""https://www.hackerrank.com/challenges/the-power-sum/problem"""

""" SMART SMART SMART"""

def power_sum(X, N, integer=1):

    res = integer ** N
    if res == X:
        return 1
    elif res > X:
        return 0
    else:
        with_integer = power_sum(X - res, N, integer + 1)
        without_integer = power_sum(X, N, integer + 1)

        return with_integer + without_integer


























# int powerSum(int X, int P, int N=1) {
#     int i_pow = pow(N,P);
#     if (i_pow > X)
#         return 0;
#     else if (i_pow == X)
#         return 1;
#       // subproblem
#     return powerSum(X,P,N+1) + powerSum(X-i_pow,P,N+1);
# }
