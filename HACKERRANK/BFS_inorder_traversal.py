
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traverse(root):
    all = []
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        all.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return all


root = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
all = inorder_traverse(root)
print(all)
# print(root.val)
# print(root.left.val)
# print(root.right.val)


