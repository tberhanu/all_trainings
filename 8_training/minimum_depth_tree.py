
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    if root == None:
        return 0
    else:
        return foo(root)


def foo(root):
    """
    Runtime: 52 ms, faster than 78.56% of Python3 online submissions for Minimum Depth of Binary Tree.
    """
    if root != None and root.left == None and root.right == None:
        return 1
    if root == None:
        return float("inf")

    return min(1 + foo(root.left), 1 + foo(root.right))


root = TreeNode(1)
root.left = TreeNode(2)
print(minDepth(root))
