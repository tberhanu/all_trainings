#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

def shortest_path(network, name1, name2):
    """shortest_path(network, name1, name2) --> a function taking a NETWORK and output and array of Strings as
    a shortest path from name1 to name2
    --> Need to install networkx, and inbuilt python function
    --> Assuming the distance between adjancent names is constant for all cases so weight=1.0 assigned

    :param network: Dictionay of String as a KEY and a list of Strings as a VALUE
    :param name1: String
    :param name2: String
    :return: Array of Strings, as a shortest path from name1 to name2
    """
    graph = make_graph(network)
    path = nx.shortest_path(graph, source=name1, target=name2)
    return path


def make_graph(network):

    graph = nx.Graph()
    for node, adjacents in network.items():
        graph.add_node(node)
        for adj in adjacents:
            graph.add_edge(node, adj, weight=1.0)

    return graph


if __name__ == "__main__":
    network = {
        'Min': ['William', 'Jayden', 'Omar'],
        'William': ['Min', 'Noam'],
        'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
        'Ren': ['Jayden', 'Omar'],
        'Amelia': ['Jayden', 'Adam', 'Miguel'],
        'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
        'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
        'Noam': ['Nathan', 'Jayden', 'William'],
        'Omar': ['Ren', 'Min', 'Scott']
    }
    print(shortest_path(network, "Jayden", "Adam"))
    print(shortest_path(network, "Adam", "Omar"))
    print(shortest_path(network, "Liam", "Nathan"))
    print(shortest_path(network, "Liam", "William"))

