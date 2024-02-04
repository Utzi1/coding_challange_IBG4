"""
File: test_adjacency_class.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Tests for the class AdjMat defined in ../../adjacency_class.py
"""

# import pytest
import adjacency_class


def test_adjmat():
    """
    Just test if the initial matrix is zeros
    and that stuff is added correctly
    """
    amatrx = adjacency_class.AdjMat(2)
    # to check if it got initialised correctly:
    assert sum(sum(amatrx.adjmat, [])) == 0

    # now fill the matrix with a single edge:
    amatrx.add_edge(0, 1)
    # and check if only one was added:
    assert sum(sum(amatrx.adjmat, [])) == 1
    # and that it was added correctly:
    assert amatrx.adjmat[0][1] == 1
