
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):

    def helper(root):
        if root is None:
            return 0


        lefty = is_balanced(root.left)
        righty = is_balanced(root.right)

        if lefty == -1 or righty == -1:
            return -1
        if abs(lefty - righty) > 1:
            return -1

        else:
            return max(lefty, righty) + 1



    return helper(root) != -1

def is_symetric(root1, root2):

    if root1.val != root2.val:
        return False
    return is_symetric(root1.left, root2.left) and is_symetric(root1.right, root2.right)

