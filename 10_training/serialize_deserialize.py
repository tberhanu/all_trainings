class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    level = 0
    arr = []
    return foo(node, level, arr)

def foo(node, level, arr):
    if node is None:
        return
    string = str(node.val)
    if level < len(arr):
        arr[level] += string
    else:
        arr.append(string)
    foo(node.left, level + 1, arr)
    foo(node.right, level + 1, arr)

    return "".join(arr)

def deserialize(string):
    index = 0
    node = Node(-99)
    dummy = node
    foo2(string, index, node)
    return dummy


def foo2(string, index, node):
    if index >= len(string):
        return
    s = string[index]
    node.val = int(s)
    lefty = foo2(string, index * 2 + 1, Node(-99))
    righty = foo2(string, index * 2 + 2, Node(-99))

    node.left = lefty
    node.right = righty
    return node



string = "1234567890"
node = deserialize(string)
string = serialize(node)
print(string)


