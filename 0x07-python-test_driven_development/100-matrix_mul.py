#!/usr/bin/python3
"""Thus module contain a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Calculates the product of two matrices m_a and m_b.

    Args:
    m_a: a list of lists of integers or floats
    m_b: a list of lists of integers or floats

    Returns:
    The product of the two matrices m_a and m_b as a list of lists.

    Raises:
    TypeError: if m_a or m_b is not a list or if m_a or m_b is
    not a list of lists
    or if one element of those list of lists is not an integer or a float or
    if m_a or m_b is not a rectangle (all 'rows' should be of the same size).

    ValueError: if m_a or m_b is empty (it means: = [] or = [[]]) or
    if m_a and m_b can't be multiplied.
    """
    """validates if m_a is not a list"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")

    """#checks if m_a is not a list of lists"""
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")

    """#checks if m_a is empty"""
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")

    """#checks if all element in m_a are int or float"""
    if not all(isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")

    """#checks if all rows of m_a are of the same size"""
    row_length = len(m_a[0])
    if not all(len(i) == row_length for i in m_a):
        raise TypeError("each row of m_a must be of the same size")

    """#checks is m_b is a list"""
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    """#checks if m_b is a list of list"""
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    """#checks if m_b is empty"""
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    """#checks if element in m_b are int or floats"""
    if not all(isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")

    """#checks if m_a and m_b can be multiplied"""
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """#Initialize the result"""
    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    """#multiply matricec m_a and m_b and store the result in result"""
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
