"""
Assessment 3.6 - DFS Method in Tree
Name: DANE ABAQUITA

Based on the full-name binary tree from Assessment 3.5.
Methods:
1. PreOrder  - Root, Left, Right
2. InOrder   - Left, Root, Right
3. PostOrder - Left, Right, Root
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """
    Build the tree from DANE ABAQUITA in level order:

                    D
                  /   \\
                 A     N
                / \\   / \\
               E   A B   A
              / \\ / \\ /
             Q  U I T A
    """
    root = Node("D")

    root.left = Node("A")
    root.right = Node("N")

    root.left.left = Node("E")
    root.left.right = Node("A")

    root.right.left = Node("B")
    root.right.right = Node("A")

    root.left.left.left = Node("Q")
    root.left.left.right = Node("U")

    root.left.right.left = Node("I")
    root.left.right.right = Node("T")

    root.right.left.left = Node("A")

    return root


def preorder(root):
    """Root -> Left -> Right."""
    result = []

    def visit(node):
        if node is None:
            return
        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def inorder(root):
    """Left -> Root -> Right."""
    result = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result


def postorder(root):
    """Left -> Right -> Root."""
    result = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        visit(node.right)
        result.append(node.value)

    visit(root)
    return result


def main():
    root = build_tree()

    print("=" * 55)
    print("ASSESSMENT 3.6 - DFS METHOD IN TREE")
    print("Name: DANE ABAQUITA")
    print("=" * 55)

    print("\\nBINARY TREE:")
    print("             D")
    print("           /   \\\\")
    print("          A     N")
    print("         / \\\\   / \\\\")
    print("        E   A B   A")
    print("       / \\\\ / \\\\ /")
    print("      Q  U I T A")

    print("\\nPREORDER TRAVERSAL")
    print("Root -> Left -> Right")
    print(" -> ".join(preorder(root)))

    print("\\nINORDER TRAVERSAL")
    print("Left -> Root -> Right")
    print(" -> ".join(inorder(root)))

    print("\\nPOSTORDER TRAVERSAL")
    print("Left -> Right -> Root")
    print(" -> ".join(postorder(root)))

    print("\\n" + "=" * 55)
    print("DFS TRAVERSAL COMPLETED SUCCESSFULLY!")
    print("=" * 55)


if __name__ == "__main__":
    main()
