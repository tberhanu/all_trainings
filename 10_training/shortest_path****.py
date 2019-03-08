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
