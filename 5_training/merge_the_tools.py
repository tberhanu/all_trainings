# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    """ TECHNIQUES USED:
    (1) The method setdefault() is similar to get(), but will set dict[key] = default if key is not already in dict.
    So, it does TWO JOBS, receiving input and providing output at the same time.

    (2) [1, 2, 3] * 2 => [1, 2, 3, 1, 2, 3]
    (3) * just before [iter(string)] is used to UNPACK to be zipped

    """
    for part in zip(*[iter(string)] * k):
        dict = {}
        concatenated = ''.join(dict.setdefault(c, c) for c in part if c not in dict)
        print(concatenated)


str = "aabcaaada"
merge_the_tools(str, 3)


# def merge_the_tools(string, k):
#
#     start = 0
#     diff = (len(string) / k) + 1
#     arr = []
#     end = start + int(diff) - 1
#
#     while end - 1 < len(string):
#         str = string[start:end]
#         unique = get_uniques(str)
#         arr.append(unique)
#         start = end
#         end = start + int(diff) - 1
#     for a in arr:
#         print(a)
#
# def get_uniques(str):
#     sets = set()
#     save = ""
#     for s in str:
#         if len(sets) == 0:
#             save = s
#             sets.add(s)
#         elif s not in sets:
#             save = save + s
#             sets.add(s)
#     return save
#
#
# print(merge_the_tools("aabcaaada", 3))