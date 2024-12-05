## Understanding the Island Perimeter Problem

**Problem Statement:**
Given a 2D grid map of `0`s (water) and `1`s (land), find the perimeter of the island. 

**Example:**
```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0]]

Output: 16
```

**Approach:**

1. **Iterate Over the Grid:**
   - Traverse each cell of the grid.
2. **Identify Land Cells:**
   - If a cell is a land cell (`1`), check its adjacent cells.
3. **Calculate Perimeter Contribution:**
   - For each land cell, count the number of its adjacent cells that are water cells (`0`).
   - Each adjacent water cell contributes 1 to the perimeter.
4. **Sum Up Contributions:**
   - Sum up the contributions from all land cells to get the total perimeter.

**Python Implementation:**

```python
def islandPerimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
```

**Explanation:**

1. **Initialize Perimeter:** The `perimeter` is initialized to 0.
2. **Iterate Over Grid:** We iterate over each cell in the grid.
3. **Identify Land Cells:** If the current cell is a land cell (`1`), we add 4 to the perimeter. This assumes that all sides of the land cell contribute to the perimeter initially.
4. **Subtract for Adjacent Land Cells:**
   - If the cell above or to the left is also a land cell, it means that one side of the current cell is shared with another land cell, so we subtract 2 from the perimeter.
5. **Return Perimeter:** After iterating through all cells, the final `perimeter` value is returned.

This approach efficiently calculates the perimeter by considering each land cell's contribution and adjusting for shared edges with adjacent land cells.
