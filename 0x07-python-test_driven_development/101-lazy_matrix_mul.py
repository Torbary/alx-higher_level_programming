#!/usr/bin/python
"""import numppy to solve matrix"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy
    
    Parameters:
    matrix1 (numpy.ndarray): First matrix to be multiplied
    matrix2 (numpy.ndarray): Second matrix to be multiplied
    
    Returns:
    numpy.ndarray: Resultant matrix after multiplying two matrices
    """
    return np.dot(m_a, m_b)
