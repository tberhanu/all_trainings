
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#14/17 test cases failed

def substrCount(n, string):
    arr = []
    save = ""
    k = 0
    for s in string:
        if save == "":
            save = s
        elif s in save:
            save = save + s
            if k == len(string) - 1:
                arr.append(save)
        else:
            arr.append(save)
            save = s
            if k == len(string) - 1:
                arr.append(save)
        k = k + 1
    i = 0
    cntr = 0
    while i < len(arr):
        # if len(arr[i]) == 1:
        cntr = cntr + get_count(arr, i)
        i = i + 1

    cntr2 = sum(len(a) * (len(a) + 1)/2 for a in arr)
    return int(cntr + cntr2)

def get_count(arr, i):
    left = i - 1
    right = i + 1
    cntr = 0
    char = arr[left]
    while left >= 0 and right < len(arr):
        if arr[left] == arr[right] and arr[left] == char:
            cntr = cntr + 1
            left = left - 1
            right = right + 1
        else:
            return cntr
    return cntr

str = "asasd"
print(substrCount(len(str), str))
str = "aaaa"
print(substrCount(len(str), str))







