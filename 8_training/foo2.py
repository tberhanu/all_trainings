
def foo(num):

    s = str(abs(num))
    ss = s[::-1]
    if num < 0:
        ss = "-" + ss
    return int(ss)





print(foo(123))
print(foo(-123))