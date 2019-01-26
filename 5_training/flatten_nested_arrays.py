from collections import Iterable
def flatten(arr):
    for a in arr:
        if isinstance(a, Iterable):
            yield from flatten(a)
        else:
            yield a


