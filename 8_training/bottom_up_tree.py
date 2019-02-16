"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order_top_to_bottom(root):
    """Runtime: 40 ms, faster than 99.36% of Python3 online submissions for Binary Tree Level Order
    Traversal II.
    But CAN YOU DO THIS PROBLEM WITH BOTTOM UP APPROACH without using [::] ??????
"""
    level = 0
    arr = []
    return foo(root, level, arr)


def foo(root, level, arr):
    if root == None:
        return
    if level == 0 or level >= len(arr):
        arr.append([root.val])
    elif level < len(arr):
        arr[level].append(root.val)

    foo(root.left, level + 1, arr)
    foo(root.right, level + 1, arr)
    return arr[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(level_order_top_to_bottom(root))
