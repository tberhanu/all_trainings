""" 222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        lefty = self.countNodes(root.left)
        righty = self.countNodes(root.right)
        return 1 + lefty + righty
