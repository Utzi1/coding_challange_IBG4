"""
File: adjacency_class.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: The class defined here only helps to provide adjacency matrices
in a convenient way and also on a personal level a little of a dummy for ttd
"""

class AdjMat:
    """A simple class to create and manipulate adjacency matrices"""
    def __init__(self, nodes):
        # the initial matrix:
        self.nodes = nodes
        self.adjmat = [[0 for i in range(nodes)] for j in range(nodes)]

    def add_edge(self, start, end):
        """Adds edges between nodes into the adjmat

        :start: the node we start at, the parent
        :end: the child node, the one the edge ends at
        :returns: TODO

        """
        self.adjmat[start][end] = 1
