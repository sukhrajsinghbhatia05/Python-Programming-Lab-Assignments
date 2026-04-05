"""
================================================================================
Practical No: 4
Lab Assignment: 1
Title: NumPy Identity Matrix and Matrix Operations

AIM:
    To perform operations using NumPy including creating identity matrix,
    generating random matrices, and performing matrix addition and multiplication.
================================================================================
"""

import numpy as np

print("=" * 70)
print(" " * 20 + "NUMPY MATRIX OPERATIONS")
print("=" * 70)

print("\n(a) 4×4 Identity Matrix:")
print("-" * 70)
identity_matrix = np.eye(4, dtype=int)
print(identity_matrix)

print("\n(b) Two 3×3 Random Matrices:")
print("-" * 70)

matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\n(c) Matrix Addition (Matrix 1 + Matrix 2):")
print("-" * 70)
matrix_sum = matrix1 + matrix2
print(matrix_sum)

print("\n(d) Matrix Multiplication (Matrix 1 × Matrix 2):")
print("-" * 70)
matrix_product = np.matmul(matrix1, matrix2)
print(matrix_product)

print("\n" + "=" * 70)
