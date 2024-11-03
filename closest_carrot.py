# closest carrot
# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid,
# 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing
# the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right,
# but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.

from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    """
    Finds the length of the shortest path from the starting position to a carrot in the grid.

    The function uses breadth-first search (BFS) to explore the grid and find the shortest path
    from the starting position to a carrot.

    Args:
        grid (list of list of str): A 2D grid where 'O' represents an open space, 'X' represents a wall,
                                    and 'C' represents a carrot.
        starting_row (int): The row index of the starting position.
        starting_col (int): The column index of the starting position.

    Returns:
        int:    The length of the shortest path from the starting position to a carrot.
                Returns -1 if there is no possible path to a carrot.
    """
    # Define the directions to move: up, down, left, right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Initialize a deque for BFS with the starting position and path length
    queue = deque([(starting_row, starting_col, 0)])
    # Initialize a set to keep track of visited positions
    visited = set()
    # Iterate while the queue is not empty
    while queue:
        # Get the current position and path length from the queue
        row, col, length = queue.popleft()
        # Check if the current position is a carrot
        if grid[row][col] == 'C':
            return length  # Return the path length if a carrot is found
        # Mark the current position as visited
        visited.add((row, col))
        # Explore all possible directions from the current position
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check if the new position is within the grid and not a wall or visited
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 'X' and (new_row, new_col) not in visited:
                # Add the new position and path length to the queue
                queue.append((new_row, new_col, length + 1))
    return -1  # Return -1 if no path to a carrot is found

grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4

grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 0, 0)) # -> 5

grid = [
    ['O', 'O', 'X', 'X', 'X'],
    ['O', 'X', 'X', 'X', 'C'],
    ['O', 'X', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'C', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 3, 4)) # -> 9

grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
]

print(closest_carrot(grid, 1, 4)) # -> 2

grid = [
    ['O', 'O', 'X', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['O', 'X', 'C', 'C', 'O'],
]

print(closest_carrot(grid, 2, 0)) # -> -1

grid = [
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
]

print(closest_carrot(grid, 0, 0)) # -> -1

grid = [
    ['O', 'O', 'X', 'C', 'O'],
    ['O', 'X', 'X', 'X', 'O'],
    ['C', 'X', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 2, 2)) # -> 5
