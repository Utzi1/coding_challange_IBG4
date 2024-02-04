"""
File: test_node_depth.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Tests for testing the node-depth method
"""


import pytest
# and the adjacency matrix helpers:
from adjacency_class import AdjMat

# and also import our algorithm that's about to be tested
from compute_node_depth import node_depth


def test_node_depth():
    """Tests the node depth function
    """
    # correct input case
    mat = AdjMat(5)
    mat.add_edge(0, 1)
    mat.add_edge(1, 2)
    mat.add_edge(2, 3)
    mat.add_edge(3, 4)
    mat.add_edge(0, 4)
    assert node_depth(mat.adjmat, 0) == 0
    assert node_depth(mat.adjmat, 1) == 1
    assert node_depth(mat.adjmat, 2) == 2
    assert node_depth(mat.adjmat, 3) == 3
    assert node_depth(mat.adjmat, 4) == 1

    # faulty input-cases:
    mat = AdjMat(5)
    # a cycle
    mat.add_edge(0, 0)

    with pytest.raises(Exception) as excinfo:
        node_depth(mat.adjmat, 0)
    assert "Adjacency matrix does not meet assumptions" in str(excinfo.value)

    # test for behaviour with non-existent (out of bound) nodes
    # where we'll just create an empty matrix
    mat = AdjMat(1)

    with pytest.raises(Exception) as excinfo:
        node_depth(mat.adjmat, 3)
    assert "Node is out of bound" in str(excinfo.value)

    # In case of a node without connecting edges
    mat = AdjMat(2)

    with pytest.raises(Exception) as excinfo:
        node_depth(mat.adjmat, 1)
    assert "Node could not be reached" in str(excinfo.value)


