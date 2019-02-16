"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
"""
Runtime: 40 ms, faster than 79.58% of Python3 online submissions for GenerateParentheses.

"""
def generate_parenthesis(n):
    """ Here we use BACK TRACKING, a technique used to look for multiple answers via
    brute force approach. Both back tracking and dynamic programming uses brute force but
    here is their difference.
    Note: DYNAMIC PROGRAMMING is for OPTIMIZATION PROBLEM, to get the highest/smallest
    Note: BACK TRACKING is for multiple answers
    """

    str = ""
    arr = []
    open, close = n, n
    return foo(n, str, arr, open, close)


def foo(n, str, arr, open, close):

    if open > 0:
        foo(n, str + "(", arr, open - 1, close)

    if close > open:
        foo(n, str + ")", arr, open, close - 1)

    if open == 0 and close == 0:
        arr.append(str)
    return arr


print(generate_parenthesis(3))

""" Best examples of BACKTRACKING """
def inorder(root):
    """ left, top, right """
    if root == None:
        return
    inorder(root.left)
    root.process()
    inorder(root.right)
def preorder(root):
    """ top, left, right """
    if root == None:
        return
    root.process()
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    root.process()
def dfs(root):
    """ DFS is recursive, while BFS is iterative using Queue """
    if root == None:
        return
    root.process()
    root.marked()
    for adj in root.adjs():
        if not adj.marked():
            dfs(adj)


def bfs(root):
    queue = [root]
    root.marked()
    while len(queue) != 0:
        node = queue.pop(0)
        del queue[0]
        node.process()
        for adj in node.adjs:
            if not adj.marked():
                queue.append(adj)
                adj.marked()
