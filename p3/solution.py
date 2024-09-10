import itertools


# Function to check if a set of vertices form a clique
def is_clique(graph, vertices):
    for u, v in itertools.combinations(vertices, 2):
        if v not in graph[u]:
            return False
    return True


# Function to check if the remaining vertices form a valid tail connected to the clique
def is_valid_tail(graph, clique, tail):
    # Check if the tail is connected to one vertex in the clique
    connected_to_clique = any([v for v in clique if any(u in graph[v] for u in tail)])
    if not connected_to_clique:
        return False

    # Check if the tail forms a simple path (no repeated edges)
    for i in range(len(tail) - 1):
        if tail[i + 1] not in graph[tail[i]]:
            return False

    return True


# Function to find if a KITE exists in the graph
def find_kite(graph, K):
    vertices = list(graph.keys())

    # Try every possible combination of K vertices for the clique
    for clique_vertices in itertools.combinations(vertices, K):
        clique_vertices = set(clique_vertices)
        remaining_vertices = set(vertices) - clique_vertices

        # Check if the selected K vertices form a clique
        if is_clique(graph, clique_vertices):
            # Try every possible combination of K vertices from the remaining vertices for the tail
            for tail_vertices in itertools.combinations(remaining_vertices, K):
                tail_vertices = list(tail_vertices)

                # Check if the remaining vertices form a valid tail
                if is_valid_tail(graph, clique_vertices, tail_vertices):
                    return True  # KITE found

    return False  # No KITE found


if __name__ == "__main__":

    graph = {
        0: {1, 2},
        1: {0, 2},
        2: {0, 1, 3},
        3: {2, 4},
        4: {3, 5},
        5: {4},
    }

    K = 3

    if find_kite(graph, K):
        print("KITE found!")
    else:
        print("No KITE found.")
