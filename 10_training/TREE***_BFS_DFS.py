""" Remember DFS is RECURSIVE APPROACH so you may need to call another function"""
def dfs(node):
    visited = set()
    return DFS(node, visited)

def DFS(node, visited):

    node.process()
    visited.add(node)

    for adj in node.adjs():
        if adj not in visited:
            DFS(adj, visited)


""" Remember BFS is ITERATIVE APPROACH so you may not need to call another function, rather you may 
    need more LOOPS and QUEUE.
"""

def bfs(node):
    visited = set()
    queue = []
    queue.append(node)

    while queue:
        node = queue.pop(0)
        node.process()
        visited.add(node)
        for adj in node.adjs():
            if adj not in visited:
                queue.append(adj)


""" ****************       SHORTEST PATH FROM node1 to node2: Using BFS   ***********************"""
def shortest_path_DFS(node1, node2):
    shortest = {node1: [node1]}  # this is the smart line of this code
    visited = set()
    queue = []
    queue.append(node1)

    while queue:

        node = queue.pop(0)
        visited.add(node)
        for adj in node.adjs():
            shortest[adj] = shortest[node] + [adj] # this is the smart line of this code
            if adj == node2:
                return shortest[adj] # ***Here you can return TRUE if asked only to check bool(ROUTE EXISTENCE)
            if adj not in visited:
                queue.append(adj)

    return None        # ***Here you can return FALSE if asked only to check bool(ROUTE EXISTENCE)

""" *******************      Check if there is a path b/n node1 to node2: Using DFS   ***************************"""

def shortest_path_dfs(node1, node2):
    seen = set()
    return is_connected(node1, node2, seen)

def is_connected(node1, node2, seen):
    if node1 == node2:
        return True
    for adj in node1.adj():
        if adj == node2:
            return True
        if adj not in seen:
            seen.add(adj)
            return is_connected(adj, node2, seen)


"""" Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height: ****    PRE ORDER TRAVERSAL  *********
  
"""
class TreeNode:
    pass
def create_minimal_BST(arr):
    start, end = 0, len(arr) - 1
    return create_BST(arr, start, end)

def create_BST(arr, start, end):
    if start > end:
        return None

    mid = (end + start + 1) // 2
    root = TreeNode(mid)

    lefty = create_BST(arr, start, mid - 1)
    righty = create_BST(arr, mid + 1, end)

    root.left = lefty
    root.right = righty

    return root

""" LIST OF DEPTHS: Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth(e.g. if you have a tree with depth D, you'll have D linked lists)
"""
class LinkedList:
    pass
def create_level_linked_list(root):
    level = 0
    dict = {}
    return get_LL(root, level, dict)

def get_LL(root, level, dict):
    if root is None:
        return
    if level in dict:
        dict[level].next = LinkedList(root.val)
    else:
        dict[level] = LinkedList(root.val)

    get_LL(root.left, level + 1, dict)
    get_LL(root.right, level + 1, dict)

    return dict

""" Check if the BST is Balanced or not Balanced  """
def isBalanced(root):
    return is_balanced(root) != -1

def is_balanced(root):
    if root is None:
        return 0

    lefty = isBalanced(root.left)
    righty = isBalanced(root.right)

    if lefty == -1 or righty == -1:
        return -1
    elif abs(lefty - righty) > 1:
        return -1
    else:
        return max(lefty, righty) + 1



""" VALIDATE BST: Implement a function to check if a binary tree is a binary search tree: 

"""

def is_BST(root):
    if root is None:
        return True
    if (root.left and root.left.val > root.val) or (root.right and root.right.val < root.val):
        return False


    lefty = is_BST(root.left)
    if lefty == False:        # this if statement is just to make it a little bit faster
        return False
    righty = is_BST(root.right)
    if righty == False:       # this if statement is just to make it a little bit faster
        return False


    return lefty and righty

def is_BST_shorter(root):
    if root == None:
        return True
    if (root.left and root.left.val > root.val) or (root.right and root.right.val < root.val):
        return False
    return is_BST_shorter(root.left) and is_BST_shorter(root.right)


####################################################################################################

def build_order(projects, depedencies):
    """ Green Book: Page 250.
        BUILD ORDER: You are given a list of projects and a list of dependencies(which is a list of pairs of
        projects, where the second project is dependent on the first project). All of a project's dependencies
        must be built before the project is. Find a build order that will allow the projects to be built. If there
        is no valid build order, return an ERROR.
        Example:
            Input: projects: a, b, c, d, e, f
                   Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
            Output: f, e, a, b, d, c



            *** Note from Tess:
                This question would be convenient if we could map the dependencies with the Dictionary, but
                it has multiple identical keys which might take us to make a GRAPH .......
    """
    pass

####################################################################################################
def first_common_ancestor(root, p, q):
    """
     First Common Ancestor of BINARY SEARCH TREE of node p and node q
    """
    if p.val < root.val and q.val < root.val:
        return first_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return first_common_ancestor(root.right, p, q)
    else:
        return root

def lowest_common_ancestor(root, p, q):
    """236. Lowest Common Ancestor of a Binary Tree
    Lowest Common Ancestor of BINARY TREE, not neccessarily BST

    Runtime: 88 ms, faster than 68.30% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

    """

    if root is None:
        return None
    if root == p or root == q:
        return root

    lefty = lowest_common_ancestor(root.left, p, q) # We TRUST our func will bring us the lowest ancestor or None
    righty = lowest_common_ancestor(root.right, p, q) # We TRUST, it'll bring us the lowest ancestor or None

    if lefty and righty: # If both side bring a NODE, then the Ancestor is their parent ROOT
        return root

    else:
        return lefty or righty # Otherwise, either of one will bring us the answer


def is_leaf(root):
    return root.left == None and root.right == None

####################################################################################################


def is_subtree(t1, t2):
    """ CHECK SUBTREE: T1 and T2 are two very large binary trees, with T1 much bigger thatn T2. Create an
        algorithm to determine if T2 is a subtree of T1
        A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical
        to T2. That is, if you cut off the tree at node n, the two trees would be identical.
        """

    if t1 == None or t2 == None: # Double check if I misunderstood the definition of sub tree
        return False
    if t1.val == t2.val:
        return is_identical(t1, t2)
    else:
        return is_subtree(t1.left, t2.left) or is_subtree(t1.right, t2.right)

def is_identical(t1, t2):
    if t1.val != t2.val:
        return False
    return is_identical(t1.left, t2.left) and is_identical(t1.right, t2.right)

####################################################################################################


def num_of_ways(N, dict):
    """ STEPPING UP STAIRS: Given N stairs, one may step 1 or 2 step at a time. Count the number of
        different ways to finish the stairs"""
    if N <= 0:
        return 0
    if N - 1 not in dict:
        dict[N - 1] = num_of_ways(N - 1)
    if N - 2 not in dict:
        dict[N - 2] = num_of_ways(N - 2)
    return 1 + dict[N - 1] + dict[N - 2]

def numOfWays(N):
    """ STEPPING UP STAIRS: Given N stairs, one may step 1 or 2 step at a time. Count the number of
        different ways to finish the stairs"""
    dict = {0: 1, 1: 1} # It takes ONE WAY to reach Ground(0) or First Stair(1)
    return count_steps(N, dict)

def count_steps(N, dict):
    if N - 1 not in dict:
        dict[N - 1] = count_steps(N - 1, dict)
    if N - 2 not in dict:
        dict[N - 2] = count_steps(N - 2, dict)

    return count_steps(N - 1, dict) + count_steps(N - 2, dict)

#################################################################
""" PATHS WITH SUM: Design an algorithm to count the number of paths that sum up to a given TARGET value
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def num_of_paths(root, targets, num, counter):
#     if root is None:
#         return
#
#     for target in targets:
#         targets.append(target - root.val)
#     if 0 in targets:
#         counter.append(1)
#
#     num_of_paths(root.left, targets, num, counter)
#     num_of_paths(root.right, targets, num, counter)
#
#     return len(counter)
#
#
# a = Tree(3, Tree(3), Tree(-2))
# b = Tree(5, a, Tree(2, None, Tree(1)))
# root = Tree(10, b, Tree(-3, None, Tree(11)))
# targets = []
# print(num_of_paths(root, targets, 18, []))
# print(num_of_paths(root, targets, 8, []))

