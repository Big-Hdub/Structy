# longest path
# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph.
# The function should return the length of the longest path within the graph. A path may start
# and end at any two nodes. The length of a path is considered the number of edges in the path,
# not the number of nodes.

def longest_path(graph):
    """
    Finds the length of the longest path within a directed acyclic graph.

    The function uses dynamic programming to calculate the length of the longest path
    starting from each node in the graph.

    Args:
        graph (dict): An adjacency list representing a directed acyclic graph.

    Returns:
        int:    The length of the longest path within the graph.
    """
    def dfs(node, graph, longest_paths):
        """
        Perform a depth-first search to find the longest path starting from a given node.

        Args:
            node (any): The starting node for the DFS.
            graph (dict): A dictionary representing the adjacency list of the graph.
            longest_paths (dict): A dictionary to store the longest path length from each node.

        Returns:
            int: The length of the longest path starting from the given node.
        """
        # If the longest path from this node is already computed, return it
        if node in longest_paths:
            return longest_paths[node]

        # Initialize the maximum length to 0
        max_length = 0

        # Iterate over each neighbor of the current node
        for neighbor in graph[node]:
            # Recursively find the longest path from the neighbor
            attempt = 1 + dfs(neighbor, graph, longest_paths)
            # Update the maximum length if the current attempt is longer
            if attempt > max_length:
                max_length = attempt

        # Store the computed longest path length for the current node
        longest_paths[node] = max_length

        # Return the longest path length from the current node
        return max_length

    # Initialize a dictionary to store the length of the longest path starting from each node
    longest_paths = {}
    # Iterate over each node in the graph
    for node in graph:
        # Calculate the length of the longest path starting from the current node
        longest_paths[node] = dfs(node, graph, longest_paths)
    # Return the maximum length of the longest path
    return max(longest_paths.values())

graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': []
}

print(longest_path(graph)) # -> 2

graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': [],
    'q': ['r'],
    'r': ['s', 'u', 't'],
    's': ['t'],
    't': ['u'],
    'u': []
}

print(longest_path(graph)) # -> 4

graph = {
    'h': ['i', 'j', 'k'],
    'g': ['h'],
    'i': [],
    'j': [],
    'k': [],
    'x': ['y'],
    'y': []
}

print(longest_path(graph)) # -> 2

graph = {
    'a': ['b'],
    'b': ['c'],
    'c': [],
    'e': ['f'],
    'f': ['g'],
    'g': ['h'],
    'h': []
}

print(longest_path(graph)) # -> 3

graph = {
    'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
    'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
    'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
    'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
    't': ['u', 'v', 'w', 'x', 'y', 'z'],
    'u': ['v', 'w', 'x', 'y', 'z'],
    'v': ['w', 'x', 'y', 'z'],
    'w': ['x', 'y', 'z'],
    'x': ['y', 'z'],
    'y': ['z'],
    'z': []
}

print(longest_path(graph)) # -> 25

# 2,4,2,3,25
