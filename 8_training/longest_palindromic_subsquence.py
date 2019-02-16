def foo(string):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1
    i, j = 0, len(string) - 1
    if string[i] == string[j]:
        return 2 + foo(string[i+1:j])
    else:
        return max(foo(string[i:j]), foo(string[i+1:j+1]))


print(foo("adbbca"))
print(foo("adbgcfbea"))
