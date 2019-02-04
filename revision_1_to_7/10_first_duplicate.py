"""
10. Given an array of elements, return the first duplicated element
"""
def first_duplicate(arr):

    sets = set()
    for a in arr:
        if a in sets:
            return a
        sets.add(a)
    return -1







print(first_duplicate("abebe"))
print(first_duplicate(list("abedfisok")))