# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land.
# The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

def minimum_island(grid):
    """
    Finds the size of the smallest island in a given grid.

    An island is defined as a group of horizontally or vertically connected 'L' cells
    (land cells). The function uses depth-first search (DFS) to explore each island
    and determine its size.

    Args:
        grid (list of list of str): A 2D grid where 'L' represents land and 'W' represents water.

    Returns:
        int: The size of the smallest island. If there are no islands, returns infinity.
    """
    # Helper function to perform depth-first search
    def dfs(i, j):
        """
        Perform a depth-first search (DFS) to count the size of an island.

        Args:
            i (int): The row index of the current cell.
            j (int): The column index of the current cell.

        Returns:
            int:    The size of the island connected to the cell at (i, j).
                    Returns 0 if the cell is out-of-bounds or is water ('W').
        """
        # Check for out-of-bounds or water cell
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
            return 0
        # Mark the cell as visited by setting it to 'W'
        grid[i][j] = 'W'
        # Recursively visit all connected land cells and count them
        return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    min_size = float('inf')  # Initialize minimum size to infinity
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell is land, perform DFS to find the island size
            if grid[i][j] == 'L':
                min_size = min(min_size, dfs(i, j))  # Update minimum size if necessary
    return min_size  # Return the size of the smallest island

# Test cases
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
print(minimum_island(grid)) # -> 2

grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]
print(minimum_island(grid)) # -> 1

grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]
print(minimum_island(grid)) # -> 9

grid = [
    ['W', 'W'],
    ['L', 'L'],
    ['W', 'W'],
    ['W', 'L']
]
print(minimum_island(grid)) # -> 1
