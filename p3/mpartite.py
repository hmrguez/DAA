import itertools


class MPartiteGraph:
    def __init__(self, partitions):
        """
        Initialize an m-partite graph with partitions.
        partitions: a list of lists, where each sublist represents a partition and contains the vertices in that partition.
        """
        self.partitions = partitions
        self.graph = {}

        # Initialize adjacency list for the graph
        for partition in partitions:
            for node in partition:
                self.graph[node] = []

    def add_edge(self, u, v):
        """
        Add an undirected edge between vertices u and v.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_clique(self, vertices):
        """
        Check if the given set of vertices forms a clique.
        """
        for u, v in itertools.combinations(vertices, 2):
            if v not in self.graph[u]:
                return False
        return True

    def find_k_clique(self, k):
        """
        Find a k-clique by selecting one vertex from each of the k partitions.
        """
        for partition_comb in itertools.combinations(self.partitions, k):
            for vertex_comb in itertools.product(*partition_comb):
                if self.is_clique(vertex_comb):
                    return vertex_comb
        return None

    def dfs(self, start, path_length, forbidden_vertices):
        """
        Perform DFS from the starting vertex to find a path of the given length.
        Ensure that the path does not include any vertices from forbidden_vertices.
        """
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            if len(path) == path_length:
                return path
            for neighbor in self.graph[vertex]:
                if neighbor not in path and neighbor not in forbidden_vertices:
                    stack.append((neighbor, path + [neighbor]))
        return None

    def find_kite(self, k):
        """
        For each k-clique found, try to find a path of length k that starts at one of the vertices in the clique
        but does not include any vertices from the clique.
        """
        # Find a k-clique
        clique = self.find_k_clique(k)
        if clique:
            print(f"Found a {k}-clique: {clique}")

            # Try to find a valid path of length k that does not include any clique vertices
            for vertex in clique:
                path = self.dfs(vertex, k+1, forbidden_vertices=set(clique))
                if path:
                    print(f"Found a valid path of length {k}: {path}")
                    return clique, path[1:]

        print(f"No valid KITE structure found for k={k}.")
        return None, None


# Example usage:
# Create an m-partite graph
partitions = [
    ['A1', 'A2'],  # Partition 1
    ['B1', 'B2'],  # Partition 2
    ['C1', 'C2'],  # Partition 3
    ['D1', 'D2']  # Partition 4
    # ['E1', 'E2']  # Partition 5
]

graph = MPartiteGraph(partitions)

# Add edges to create a graph structure
graph.add_edge('A1', 'B1')
graph.add_edge('A1', 'C1')
graph.add_edge('B1', 'C1')
graph.add_edge('B2', 'C2')
graph.add_edge('A1', 'D1')
graph.add_edge('A2', 'D2')
graph.add_edge('B1', 'D1')
graph.add_edge('C1', 'D1')
graph.add_edge('C2', 'D2')
graph.add_edge('C2', 'D1')

# # Add extra edges for the path (tail of the KITE)
# graph.add_edge('D1', 'E1')
# graph.add_edge('E1', 'F1')

# Find a KITE structure (k-clique with a tail path of length k)
k = 3
clique, path = graph.find_kite(k)
if clique and path:
    print(f"KITE structure found: Clique = {clique}, Path = {path}")
else:
    print("No KITE structure found.")