"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, tree: 'TreeNode') -> 'bool':
        
        tree2 = tree
        return self.isSymmetrical(tree, tree2)

    def isSymmetrical(self, tree, tree2):

        if tree == None and tree2 == None:
            return True
        elif tree == None or tree2 == None:
            return False
        elif tree.val != tree2.val:
            return False
        else:
            return self.isSymmetrical(tree.left, tree2.right) and self.isSymmetrical(tree.right, tree2.left)
