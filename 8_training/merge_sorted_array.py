"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Don't return something else, but just IMPLICITLY modify only nums1

"""


def merge_sorted_array(num1, num2):
    # num1.sort()
    # num2.sort()
    i = 0
    j = 0
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            i = i + 1
        else:
            num1.insert(i, num2[j])
            i = i + 1
            j = j + 1

    if num2[j:]:
        num1.extend(num2[j:])


num1 = [1, 2, 3]
num2 = [2, 5, 6]
merge_sorted_array(num1, num2 )
print(num1)
num1 = [0, 2]
num2 = [1]
merge_sorted_array(num1, num2)
print(num1)
