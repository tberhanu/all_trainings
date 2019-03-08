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


