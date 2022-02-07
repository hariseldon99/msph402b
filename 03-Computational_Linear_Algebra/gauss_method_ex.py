#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:52:58 2022

@author: Analabha Roy
"""
import numpy as np


def GEPP(A, b, doPP=True):
    '''
    Gaussian elimination with partial pivoting.

    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b
            with the entries permuted in
            accordance with the pivoting
            done by the algorithm
    post-condition: A and b have been modified.
    '''
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between" +
                         "A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the
    # upper right triangle, we also use k for indicating the k-th diagonal
    # column index.

    # Elimination
    for k in range(n-1):
        if doPP:
            # Pivot
            maxindex = abs(A[k:, k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            # Swap
            if maxindex != k:
                A[[k, maxindex]] = A[[maxindex, k]]
                b[[k, maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPP to True.")
        # Eliminate
        for row in range(k+1, n):
            multiplier = A[row, k]/A[k, k]
            A[row, k:] = A[row, k:] - multiplier * A[k, k:]
            b[row] = b[row] - multiplier*b[k]
    # Back Substitution
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:]))/A[k, k]
    return x


def det(A):
    _ = GEPP(A, np.ones(A.shape[0]), doPP=True)
    return np.prod(np.diagonal(A))


if __name__ == '__main__':
    A = np.array([[25., 5., 1.],
                  [64., 8., 1.],
                  [144., 12., 1.]])

    b = np.array([106.8,
                  177.2,
                  279.2])

    x = GEPP(np.copy(A), np.copy(b), doPP=False)
    print("First solution is given by x =", x)
    print("Error is ", np.linalg.norm(A@x - b) * 100/np.linalg.norm(b), "%")

    print("Determinant of first matrix is ", det(np.copy(A)))

    A = np.array([[12., 10., -7.],
                  [6., 5., 3.],
                  [5., -1., 5.]])
    b = np.array([15.,
                  4.,
                  9.])

    try:
        x = GEPP(np.copy(A), np.copy(b), doPP=False)
    except ValueError:
        x = GEPP(np.copy(A), np.copy(b))

    print("Second solution is given by x =", x)
    print("Error is ", np.linalg.norm(A @ x - b) * 100/np.linalg.norm(b), "%")
    