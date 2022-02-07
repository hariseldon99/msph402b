#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:59:29 2022

@author: Analabha Roy
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve
A = np.array([[25., 5., 1.],
              [64., 8., 1.],
              [144., 12., 1.]])

b = np.array([106.8,
              177.2,
              279.2])

A_fact, piv = lu_factor(A.copy())

print("Decomposed L Matrix:\n", np.tril(A_fact, k=0))
print("\n\nDecomposed U Matrix:\n", np.triu(A_fact, k=1))

x = lu_solve((A_fact.copy(), piv), b)

print("\nSolution is x =", x)
print("Solution is close?", np.allclose(A @ x, b))

id = np.eye(A.shape[0])
A_inv = np.zeros_like(A)

for i, row in enumerate(id):
    A_inv[:, i] = lu_solve((A_fact.copy(), piv), row)

print("\n\nInverse of matrix is:\n", A_inv)
print("Solution is close?", np.allclose(A @ A_inv, id))
