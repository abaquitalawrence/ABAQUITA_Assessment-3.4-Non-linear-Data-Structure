"""
Assessment 3.4 - Graph Traversal
Name: ABAQUITA

A1, A2, and A3 are the three separate A vertices in ABAQUITA.
The graph is undirected. Neighbor order is listed explicitly so
the BFS and DFS output is repeatable.
"""

from collections import deque


def build_graph():
    # Each connection is represented in both directions because
    # this is an undirected graph.
    return {
        "A1": ["B", "A2"],
        "B":  ["A1", "Q", "U"],
        "A2": ["A1", "I", "T"],
        "Q":  ["B", "A3"],
        "U":  ["B", "I"],
        "I":  ["A2", "U"],
        "T":  ["A2", "A3"],
        "A3": ["Q", "T"],
    }


def breadth_first_search(graph, start):
    """Visit all reachable vertices level by level using a queue."""
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def depth_first_search(graph, start):
    """Visit one path as deeply as possible before backtracking."""
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def main():
    graph = build_graph()
    start_vertex = "A1"

    print("=" * 48)
    print("ASSESSMENT 3.4 - GRAPH")
    print("Last Name: ABAQUITA")
    print("=" * 48)

    print("Connections (undirected edges):")
    edges = [
        ("A1", "B"), ("A1", "A2"), ("B", "Q"),
        ("B", "U"), ("Q", "A3"), ("A3", "T"),
        ("T", "A2"), ("A2", "I"), ("I", "U")
    ]
    for first, second in edges:
        print(f"{first} -- {second}")

    print(f"\nStarting vertex: {start_vertex}")
    print("BFS:")
    print(" -> ".join(breadth_first_search(graph, start_vertex)))

    print("\nDFS:")
    print(" -> ".join(depth_first_search(graph, start_vertex)))


if __name__ == "__main__":
    main()
