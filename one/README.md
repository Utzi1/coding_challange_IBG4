# Usage

To use this I'd suggest to do so in a python venv.
Create a virtual environment:
`python3 -m venv test_env`

And in a next step activate it:
`source test_env/bin/acivate`

Install dependencies:
`pip install -r requirements.txt`

And run pytest:
`python pytest -m tests`

If you just want to just compute use it:
`
from adjacency_class import AdjMat 
from compute_node_depth import node_depth

# The AdjMat class helps to quickly create a adjacency matrix
mat = AdjMat(5)                      
# and add edges
mat.add_edge(0, 1)                   
mat.add_edge(1, 2)                   
mat.add_edge(2, 3)                   
mat.add_edge(3, 4)                   
mat.add_edge(0, 4)                   
# which then can be used to compute the depth of a node
node_depth(mat.adjmat, 0) == 0
`
