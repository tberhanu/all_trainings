"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def sortedArrayToBST(arr):
    """
    Runtime: 68 ms, faster than 67.41% of Python3 online submissions for Convert Sorted Array
    to Binary Search Tree.

    """
    if len(arr) == 1:
        return TreeNode(arr[0])
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])

    return root
