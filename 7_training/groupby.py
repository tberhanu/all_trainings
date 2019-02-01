""" 27. Given an array of dicts, group them with the same city/state
"""
import itertools
array_dicts = [{"name": "A", "city": "San Jose", "state": "CA", "color": "red"},
                {"name": "B", "city": "Oakland", "state": "CA", "color": "yellow"},
                {"name": "C", "city": "Vegas", "state": "NV", "color": "red"},
                {"name": "A", "city": "Seattle", "state": "WA", "color": "green"},
                {"name": "B", "city": "Cddd", "state": "NV", "color": "yellow"}]
# print(array_dicts)


def get_state(d):

    return d["color"]


print(array_dicts)
""" For groupby to work, you need to SORT it by your choice of dict key """
# array_dicts.sort(key=get_state)
array_dicts.sort(key=lambda d: d["name"])

print(array_dicts)
# group_by_state = itertools.groupby(array_dicts, get_state)
group_by_state = itertools.groupby(array_dicts, lambda d: d["name"])


for key, group in group_by_state:
    print(key)
    for g in group:
        print(g)
    print("Here -----")
