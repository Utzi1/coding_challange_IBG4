"""
File: compute_node_depth.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Definition of the function to compute the node depth
"""
import numpy as np
import networkx as nx


def node_depth(adj_mat, node, root=0):
    """
    Function that uses breadth-first-search to return the node depth of a
    given node from a adjacency matrix of a directed acyclic graph (DAG)

    :adj_mat: The adjacency matrix coding for the DAG
    :root: The root-node (defaulted with 0)
    :node: The node of which the depth is computed
    :returns: the depth of the node

    """
    # to check the assumptions quick:
    if not nx.is_directed_acyclic_graph(
        nx.from_numpy_array(
            np.array(adj_mat), create_using=nx.DiGraph())):
            raise Exception("Adjacency matrix does not meet assumptions")

    # check if node index is present:
    if node >= len(adj_mat):
        raise Exception("Node is out of bound")

    # to keep track of which nodes that are visited:
    visited = [False] * len(adj_mat)

    # and queue the nodes as tuple with their depth
    queue = [(root, 0)]

    while queue:
        # assign node and depth of the currently visited node
        current_node, depth = queue.pop(0)
        if current_node == node:
            print("node ", node, " has a depth of ", depth)
            return depth

        # next start visiting all adjacent nodes to our current root:
        if not visited[current_node]:
            # firstly keep track of the visit:
            visited[current_node] = True
            # and iterate through adjacent nodes
            for i, adjacen_node in enumerate(adj_mat[current_node]):
                if adjacen_node and not visited[i]:
                    queue.append((i, depth + 1))
    # however if the node can't be reached return -1:
    raise Exception("Node could not be reached")
