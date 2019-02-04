"""
20. Given a complete binary tree, count the number of nodes.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode

    """
    def count_nodes(self, root):
        if root is None:
            return 0
        else:
            lefty = self.count_nodes(root.left)
            righty = self.count_nodes(root.right)
            return 1 + lefty + righty


node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
solution = Solution()
print(solution.count_nodes(node))