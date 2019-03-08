def longest_common_prefix(arr):

    arr2 = [len(a) for a in arr]
    size = min(arr2)
    # print(size)
    i = 0
    all = []
    while i < size:

        e = arr[0][i]
        for k in range(len(arr)):
            if arr[k][i] != e:
                return "".join(all)

        all.append(e)
        i = i + 1

    return "".join(all)



print(longest_common_prefix(["ab", "a", "acd", "aaa"])) # "a"

print(longest_common_prefix(["abbc", "abc", "abcd"]))#""