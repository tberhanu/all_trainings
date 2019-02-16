
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bottom_up_traverse(head):
    from collections import deque
    queue = deque()
    stack = deque()
    queue.append(head)
    while len(queue) != 0:
        curr = queue.popleft()
        if curr.right is not None:
            queue.append(curr.right)
        if curr.left is not None:
            queue.append(curr.left)

        stack.append(curr.val)
    return stack

head = Tree(3, Tree(9, Tree(44), Tree(99)), Tree(20, Tree(15), Tree(7)))
stack = bottom_up_traverse(head)
while stack:
    print(stack.pop())
