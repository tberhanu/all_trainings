"""https://www.hackerrank.com/challenges/tree-level-order-traversal/problem"""
def levelOrder(root):
    # Write your code here
    level = 0
    all = []
    foo(root, level, all)
    # generator = flatten(all)
    # lst = list(generator)
    s = ""
    for a in all:
        s = s + " ".join(a) + " "
    print(s)


def foo(root, level, all):
    if root is None:
        return
    if level < len(all):
        all[level].append(str(root.info))
    else:
        all.append([str(root.info)])

    foo(root.left, level + 1, all)
    foo(root.right, level + 1, all)

# from collections.abc import Iterable
# def flatten(arr):
#     for a in arr:
#         if isinstance(a, Iterable):
#             yield from flatten(a)
#         else:
#             yield a
