"""Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    """ Runtime: 92 ms, faster than 70.96% of Python3 online submissions for Merge Two Binary Trees.

    PRE ORDER TRAVERSAL
    def foo(node):
        if node == None or node is Leaf:
            return "node_empty_case"
        process(node)
        foo(node.left)
        foo(node.right)
"""
    if not t1 and not t2:
        return None
    if t1 and t2:
        t3 = TreeNode(t1.val + t2.val)
    if t1 and not t2:
        return t1
    if t2 and not t1:
        return t2

    lefty = self.mergeTrees(t1.left, t2.left)
    righty = self.mergeTrees(t1.right, t2.right)
    t3.left = lefty
    t3.right = righty

    return t3
