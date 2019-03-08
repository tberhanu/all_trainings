
""" POST ORDER TRAVERSAL

    def foo(node):
        if node == None or node is Leaf:
            return 'sth'

        foo(node.left)
        foo(node.right)
        process(node)
"""

class BST:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(head):
    return foo(head) != -1

def foo(head):
    if head == None:
        return 0

    lefty = foo(head.left)
    righty = foo(head.right)

    if lefty == -1 or righty == -1:
        return -1
    elif abs(lefty - righty) > 1:
        return -1
    else:
        return max(lefty, righty) + 1



a = BST(3, BST(4), BST(4))
b = BST(2, a, BST(3))
head = BST(1, b, BST(2))

print(is_balanced(head))