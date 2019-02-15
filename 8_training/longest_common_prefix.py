def longest_common_prefix(arr):
    
    if arr == []:
        return ""
    elif len(arr) == 1:
        return arr[0]
    prefix = get_prefix(arr[0], arr[1])
    for i in range(2, len(arr)):
        prefix = get_prefix(prefix, arr[i])
    return prefix


def get_prefix(str1, str2):
    lst = zip(str1, str2)
    prefix = ""
    for tup in lst:
        if tup[0] != tup[1]:
            break
        else:
            prefix = prefix + tup[0]
    return prefix
############################  Better run time
def get_common(self, str, array):
    result = ""
    for s1, s2 in zip(str, array[0]):
        if s1 == s2:
            result = result + s1
        else:
            break
    if len(array) == 1:
        return result
    else:
        return self.get_common(result, array[1:])

def longestCommonPrefix(self, arr):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(arr) == 0:
        return ""
    if len(arr) == 1:
        return arr[0]
    common = self.get_common(arr[0], arr[1:])
    return common

############################################

arr = ["aca","cba"]
print(longest_common_prefix(arr))
arr = ["aa", "aa"]
print(longest_common_prefix(arr))
arr = ["flower", "flow", "flight"]
print(longest_common_prefix(arr))
arr = ["dog","racecar","car"]
print(longest_common_prefix(arr))
arr = ["flower", "flow", "flowrence"]
print(longest_common_prefix(arr))
