"""
31. Given an array of dicts, print out by the group name for like "color" or "state" and
the related group members
"""
import itertools
def group_by(arr_dicts, key):
    arr_dicts.sort(key=lambda d: d[key])
    group = itertools.groupby(array_dicts, key=lambda d: d[key])
    return group



array_dicts = [{"name": "A", "city": "San Jose", "state": "CA", "color": "red"},
                {"name": "B", "city": "Oakland", "state": "CA", "color": "yellow"},
                {"name": "C", "city": "Vegas", "state": "NV", "color": "red"},
                {"name": "A", "city": "Seattle", "state": "WA", "color": "green"},
                {"name": "B", "city": "Cddd", "state": "NV", "color": "yellow"}]

key = "state"
groups = group_by(array_dicts, key)
for key, group in groups:
    print(key)
    for g in group:
        print(g)
    print("----------------------")
print("***************************")
key = "color"
groups = group_by(array_dicts, key)
for key, group in groups:
    print(key)
    for g in group:
        print(g)
    print("----------------------")