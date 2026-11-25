"""
Assessment 3.4 - Binary Tree Traversal
Name: ABAQUITA

The repeated letter A is labeled A1, A2, and A3 so each node
can be identified separately. These labels still represent the
letters in ABAQUITA.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    # Tree structure based on Assessment 3.3:
    #
    #             A1
    #           /    \
    #          B      A2
    #         / \    /  \
    #        Q   U  I    T
    #       /
    #      A3

    root = Node("A1")

    root.left = Node("B")
    root.right = Node("A2")

    root.left.left = Node("Q")
    root.left.right = Node("U")

    root.right.left = Node("I")
    root.right.right = Node("T")

    root.left.left.left = Node("A3")

    return root


def breadth_first_search(root):
    """Visit nodes level by level using a queue."""
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result


def depth_first_search(root):
    """Preorder DFS: visit node, then left subtree, then right subtree."""
    result = []

    def visit(node):
        if node is None:
            return

        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def main():
    root = build_tree()

    print("=" * 48)
    print("ASSESSMENT 3.4 - BINARY TREE")
    print("Last Name: ABAQUITA")
    print("=" * 48)
    print("BFS (level by level):")
    print(" -> ".join(breadth_first_search(root)))

    print("\nDFS (preorder: node, left, right):")
    print(" -> ".join(depth_first_search(root)))


if __name__ == "__main__":
    main()
