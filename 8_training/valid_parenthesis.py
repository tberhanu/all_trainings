def isValid(s):
    dict = {")": "(", "]": "[", "}": "{"}
    if s == "":
        return True
    arr = list(s)
    if arr[0] in dict.keys() or arr[-1] in dict.values():
        return False
    i = 0
    while i < len(arr):

        if i - 1 >= 0 and arr[i] in dict.keys() and arr[i - 1] != dict[arr[i]]:
            return False
        elif i - 1 >= 0 and arr[i] in dict.keys() and arr[i - 1] == dict[arr[i]]:
            del arr[i - 1:i + 1]
            i = i - 2
        else:
            i = i + 1
    return arr == []

print(isValid("([[]]())"))
print(isValid("(([]])"))
