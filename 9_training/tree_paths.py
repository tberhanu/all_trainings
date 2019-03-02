"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def binary_tree_paths(root):
    if root == None:
        return []
    arr = []
    string = ""
    return foo(root, arr, string)


def foo(root, arr, string):
    if root.left is None and root.right is None:
        string = string + str(root.val)
        arr.append(string)

    if root.left:
        foo(root.left, arr, string + str(root.val) + "->")
    if root.right:
        foo(root.right, arr, string + str(root.val) + "->")
    return arr


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
result = binary_tree_paths(root)
print(result)