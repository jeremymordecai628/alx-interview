Here’s a structured guide to implementing the in-place 90-degree clockwise rotation for a 2D matrix, followed by a Python code solution.

---

### Key Steps to Rotate a 2D Matrix in Place

1. **Matrix Transposition**:
   - Swap the element at position `(i, j)` with the element at `(j, i)` for all `i < j`. This converts rows into columns.

2. **Reverse Each Row**:
   - After transposing, reverse each row to achieve the 90-degree clockwise rotation.

---

### Python Code Implementation

```python
#!/usr/bin/python3
"""
This script rotates an n x n 2D matrix by 90 degrees clockwise in place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
```

---

### Explanation of the Code

1. **Transpose the Matrix**:
   - Using nested loops, the `(i, j)` elements are swapped with `(j, i)` for all `i < j`. This ensures that rows become columns while keeping the operation in place.

2. **Reverse Each Row**:
   - After transposition, each row is reversed. This completes the clockwise rotation.

---

### Example Usage

```python
# Define a sample 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix
rotate_2d_matrix(matrix)

# Print the rotated matrix
print(matrix)
```

**Output**:
```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

---

### Space and Time Complexity

- **Time Complexity**: \(O(n^2)\), where \(n\) is the dimension of the matrix. This is due to iterating through all elements once during transposition and again during row reversal.
- **Space Complexity**: \(O(1)\), as the operation is performed in place without using extra space.

---

Mastering the concepts of transposition, row reversal, and in-place modifications will not only help with this challenge but also build a strong foundation for advanced matrix manipulations.