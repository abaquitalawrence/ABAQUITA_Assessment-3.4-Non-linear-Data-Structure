ASSESSMENT 3.4 AND 3.6 - NON-LINEAR DATA STRUCTURE
Name: DANE ABAQUITA
Language: Python 3

PROJECT FILES
1. binary_tree.py - Original Assessment 3.4 binary tree program.
2. graph.py       - Original Assessment 3.4 undirected graph program.
3. dfs_tree.py    - Assessment 3.6 DFS traversals using the full-name
                    binary tree from Assessment 3.5.
4. README.txt     - Project instructions and expected results.

IMPORTANT
The original Assessment 3.4 files, binary_tree.py and graph.py, are
preserved unchanged. Assessment 3.6 is added as a separate file.

HOW TO RUN
Open this folder in PyCharm or another Python 3 editor.
Run each program separately:

    python binary_tree.py
    python graph.py
    python dfs_tree.py

On some Windows computers, use:

    py binary_tree.py
    py graph.py
    py dfs_tree.py

ASSESSMENT 3.6 TREE
The letters in DANE ABAQUITA are placed in the tree in level order:

                    D
                  /   \
                 A     N
                / \   / \
               E   A B   A
              / \ / \ /
             Q  U I T A

EXPECTED ASSESSMENT 3.6 TRAVERSALS
PreOrder (Root, Left, Right):
D -> A -> E -> Q -> U -> A -> I -> T -> N -> B -> A -> A

InOrder (Left, Root, Right):
Q -> E -> U -> A -> I -> A -> T -> D -> A -> B -> N -> A

PostOrder (Left, Right, Root):
Q -> U -> E -> I -> T -> A -> A -> A -> B -> A -> N -> D

GITHUB SUBMISSION
After testing the new file, run these commands from this project folder:

    git add dfs_tree.py README.txt
    git commit -m "Add Assessment 3.6 DFS Method in Tree"
    git push

Run the Git commands only after opening/cloning your existing Assessment 3.4
GitHub repository folder. These commands add the new Assessment 3.6 file
to that same repository.
