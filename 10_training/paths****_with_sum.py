""" Green Book: Page 272
    PATHS WITH SUM: Design an algorithm to count the number of paths that sum up to a given TARGET value
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def num_of_paths(root, targets, num, counter):
#     if root is None:
#         return
#
#     for target in targets:
#         targets.append(target - root.val)
#     if 0 in targets:
#         counter.append(1)
#
#     num_of_paths(root.left, targets, num, counter)
#     num_of_paths(root.right, targets, num, counter)
#
#     return len(counter)
#
#
# a = Tree(3, Tree(3), Tree(-2))
# b = Tree(5, a, Tree(2, None, Tree(1)))
# root = Tree(10, b, Tree(-3, None, Tree(11)))
# targets = []
# print(num_of_paths(root, targets, 18, []))
# print(num_of_paths(root, targets, 8, []))

