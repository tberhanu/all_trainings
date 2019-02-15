def remove_duplicates(nums):
    dict = {}
    return [dict.setdefault(c, c) for c in nums if c not in dict]


def remove_duplicates_inplace(nums):
    sets = {nums[0]}
    i = 1
    while i < len(nums):
        if nums[i] not in sets:
            sets.add(nums[i])
            i = i + 1
        else:
            del nums[i]
    return len(nums)

def remove_duplicates_inplace_two(nums):
    i = 0
    while i < len(nums):
        if nums[i] in nums[:i] + nums[i+1:]:
            del nums[i]
        else:
            i = i + 1
    return len(nums)


def remove_sorted_duplicates_inplace(nums):
    i = 0
    while i + 1 < len(nums):
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i = i + 1

    return len(nums)


def removeElement(nums, val):
    i = 0
    while (i < len(nums)):
        if nums[i] == val:
            nums.pop(i)
        else:
            i = i + 1
    return len(nums)


arr = [1, 1, 2, 3, 2, 4, 5, 5, 1]
print(remove_duplicates_inplace(arr))
print(arr)
print("--------")
arr = [1, 1, 2, 3, 2, 4, 5, 5, 1]
print(remove_duplicates_inplace_two(arr))
print(arr)
