from collections import Counter, OrderedDict

class MostCommonAndAlphabeticOrder(Counter, OrderedDict):
    pass

def get_n_most_common(iterable, n):

    obj = MostCommonAndAlphabeticOrder(list(iterable))

    return obj.most_common(n)



arr = [1, 2, 3, 4, 4, 4, 3, 3]
print(get_n_most_common(arr, 2))
print(get_n_most_common("Get thee Most common letter", 2))