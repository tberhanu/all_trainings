# import fileinput
#
# for line in fileinput.input():
#     pass
import math
def foo(d1, d2):
    d3 = math.sqrt(d1*d1 + d2*d2)
    d4 = d3 / 2
    # k = math.sqrt(d4*d4 - d2*d2)
    # print(d4/k)
    angle = int(math.degrees(math.asin(d4 / d2)))
    print(str(angle) + "°")



foo(1, 10)
