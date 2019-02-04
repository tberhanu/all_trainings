"""
39. Givne arr1 and arr2, create a dict using arr1 as key and arr2 as value
"""
def create_dict(arr1, arr2):
    return dict(zip(arr1, arr2))



arr1 = ["a", "b", "c"]
arr2 = ["A", "B", "C"]
print(create_dict(arr1, arr2))
