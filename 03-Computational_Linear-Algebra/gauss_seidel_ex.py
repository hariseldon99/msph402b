#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:00:59 2022

@author: daneel
"""
import numpy as np


def gauss_seidel(A, b, tolerance=1e-10, max_iterations=100000, verbose=False):
    """
    Simple Function for the Gauss-Seidel Method for solving a system of linear
    equations
    Returns a numpy array consisting of the solution x, where A . x = b

            Parameters:
                    A (numpy array): A square matrix of coefficients
                    b (numpy array): The RHS vector of the linear system

            Returns:
                    x (numpy array): Solution to the equation A . x = b
    """
    x = np.zeros_like(b, dtype=np.double)

    if verbose:
        print("Iteration\t% soln: Relative err")
    # Iterate
    for k in range(max_iterations):
        x_old = x.copy()

        # Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) -
                    np.dot(A[i, (i+1):], x_old[(i+1):])) / A[i, i]

        error = np.linalg.norm(x - x_old,
                               ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        if verbose:
            print("%lf\t %1.4lf " % (k, error * 100))

        # Stop condition
        if error < tolerance:
            break
    if k == max_iterations - 1:
        raise StopIteration("Error: Maximum iterations exceeded", k)

    return x


def isDDM(m, n):
    """
    Checks a numpy 2d square array for diagonal dominance
    """

    # for each row
    for i in range(0, n):
        # for each column, finding sum of each row sans the diagonal
        sum = np.sum(m[i]) - np.abs(m[i, i])
        if (abs(m[i, i]) < sum):
            return False

    return True


if __name__ == '__main__':
    mat = np.array([[16, 3],
                    [7, -11]])

    rhs = np.array([11,
                    13])

    print("x =", gauss_seidel(mat, rhs, verbose=True))
    mat = np.array([[25, 5, 1],
                    [64, 8, 1],
                    [144, 12, 1]])

    rhs = np.array([106.8,
                    177.2,
                    279.2])

    print("Is matrix diagonally dominant?", isDDM(mat, 3))
    # NOTE: Uncomment the line below to induce an exception arising due to lack of diagonal dominance
    # print("x =", gauss_seidel(mat, rhs))

    mat = np.array([[12, 3, -5],
                    [1,  5,  3],
                    [3,  7, 13]])

    rhs = np.array([1,
                    28,
                    76])

    print("Is matrix diagonally dominant?", isDDM(mat, 3))
    print("x =", gauss_seidel(mat, rhs))
    mat = np.array([[1,  5,  3],
                    [12, 3, -5],
                    [3,  7, 13]])

    rhs = np.array([28,
                    1,
                    76])

    print("Is matrix diagonally dominant?", isDDM(mat, 3))

    try:
        print("x =", gauss_seidel(mat, rhs))
    except Exception:
        print("The algorithm failed to converge")
