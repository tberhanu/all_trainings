"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None

    root2 = TreeNode(root.val)
    dummy = root2
    foo(root, root2)
    return dummy

def foo(root, root2):
    if root is None:
        return

    if root.right:
        root2.left = TreeNode(root.right.val)
        foo(root.right, root2.left)
        
    if root.left:
        root2.right = TreeNode(root.left.val)
        foo(root.left, root.right)
