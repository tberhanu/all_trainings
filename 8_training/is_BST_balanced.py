"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_balanced(root):
    return foo(root) != -1


def foo(root):
    """
    Runtime: 56 ms, faster than 99.89% of Python3 online submissions for Balanced Binary Tree.
    """
    if root == None:
        return 0
    lefty = foo(root.left)
    if lefty == -1:
        return -1
    righty = foo(root.right)
    if righty == -1:
        return -1
    if abs(lefty - righty) > 1:
        return -1
    return max(lefty, righty) + 1
