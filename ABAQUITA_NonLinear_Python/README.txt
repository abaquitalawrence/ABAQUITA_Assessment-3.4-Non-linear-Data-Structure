ASSESSMENT 3.4 - NON-LINEAR DATA STRUCTURE
Last Name: ABAQUITA
Language: Python 3

FILES
1. binary_tree.py - builds the ABAQUITA binary tree and displays BFS and DFS.
2. graph.py       - builds the ABAQUITA undirected graph and displays BFS and DFS.

HOW TO RUN
1. Extract this ZIP file.
2. Open the extracted ABAQUITA_NonLinear_Python folder in VS Code, PyCharm,
   IDLE, or another Python editor.
3. Open a terminal in that folder.
4. Run these commands separately:

   python binary_tree.py
   python graph.py

   On some Windows computers, use:
   py binary_tree.py
   py graph.py

EXPECTED TRAVERSALS

BINARY TREE
BFS: A1 -> B -> A2 -> Q -> U -> I -> T -> A3
DFS (preorder): A1 -> B -> Q -> A3 -> U -> A2 -> I -> T

GRAPH
BFS: A1 -> B -> A2 -> Q -> U -> I -> T -> A3
DFS: A1 -> B -> Q -> A3 -> T -> A2 -> I -> U

IMPORTANT NOTES
- ABAQUITA contains three A letters. They are labeled A1, A2, and A3
  in the diagrams and code to distinguish the separate nodes/vertices.
- In the binary tree, DFS means preorder traversal (Root, Left, Right).
- In the graph, the neighbor order in the adjacency list determines the
  exact BFS/DFS sequence. The code uses the same order shown in this project.
- No external Python packages are required. The programs use Python's
  built-in features only.
