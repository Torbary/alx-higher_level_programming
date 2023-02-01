#!/usr/bin/python3
"""import numppy to solve matrix"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy

    Parameters:
    m_a (numpy.ndarray): First matrix to be multiplied
    m_b (numpy.ndarray): Second matrix to be multiplied

    Returns:
    numpy.ndarray: Resultant matrix after multiplying two matrices
    """
    return (np.matmul(m_a, m_b))
