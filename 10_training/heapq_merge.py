import heapq

def ordered_merge(lists):

    i = 1
    lst = lists[0]
    while i < len(lists):
        lst = list(heapq.merge(lst, lists[i]))
        i += 1
    return lst


def flatten(lsts):
    from collections.abc import Iterable
    for lst in lsts:
        if isinstance(lst, Iterable):
            yield from flatten(lst)
        else:
            yield lst


def ordered_merge_two(lists):
    lst = list(flatten(lists))
    return sorted(lst)
ls = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
# [10, 12, 15, 15, 17, 20, 20, 30, 32]

print(ordered_merge(ls))
print(list(flatten(ls)))
print(ordered_merge_two(ls))

