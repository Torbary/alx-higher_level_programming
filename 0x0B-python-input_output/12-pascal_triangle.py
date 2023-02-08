#!/usr/bin/python3
"""
contains fucntion pascal_traingle
"""


def pascal_triangle(n):
    """
        returns a list os lists of int reprresenting the
        pascal's triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]

    """loop until the number of rows equals n"""
    while len(triangles) != n:
        """Get the last row of the triangle"""
        tri = triangles[-1]
        """initialize a list to store thr next row"""
        tmp = [1]
        """cal the rest of the elem in the row"""
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        """add 1 to the last elem in the row"""
        tmp.append(1)
        """append the row to the triangle"""
        triangles.append(tmp)
    return triangles
