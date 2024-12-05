#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
        grid (list of list of int): 2D grid where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume each land cell contributes 4 to the perimeter initially
                perimeter += 4
                # Subtract 2 for each adjacent land cell (shared edge)
                if i > 0 and grid[i - 1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                    perimeter -= 2
    return perimeter
