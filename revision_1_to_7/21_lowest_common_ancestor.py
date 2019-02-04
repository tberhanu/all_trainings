"""
21. Having a complete binary tree, and given ROOT, P, and Q, find the lowest common ancestor
of P and Q Nodes.
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

    def lowest_common_ancestor(self, node, P, Q):
        pass



node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.left.left = TreeNode(6)
node1 = node.left.left.left
node.left.right = TreeNode(5)
node2 = node.left.right

print(node.lowest_common_ancestor(node, node1, node2))