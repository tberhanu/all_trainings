"""https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem"""
class Node:
    pass

def insert(self, val):
    return insert2(self.root, val)


def insert2(root, val):
    # Enter you code here.
    if root is None:
        node = Node(val)
        root = node
    elif val >= root.info:
        root.right = insert2(root.right, val)
    else:
        root.left = insert2(root.left, val)

    return root


