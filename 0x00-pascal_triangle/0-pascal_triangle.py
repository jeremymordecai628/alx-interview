#!/usr/bin/python3
"""
This module contains the PascalTriangle class,
which can generate Pascal's Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Sum of the two elements above the current element
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
