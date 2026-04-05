"""
================================================================================
Practical No: 4
Lab Assignment: 2
Title: Matrix Multiplication Using NumPy

AIM:
    To develop a NumPy program to multiply a 5×3 matrix by a 3×2 matrix and
    create a product matrix.
================================================================================
"""

import numpy as np

print("=" * 70)
print(" " * 20 + "MATRIX MULTIPLICATION")
print("=" * 70)

print("\nEnter elements for 5×3 Matrix:")
print("-" * 70)
matrix_5x3 = []
for i in range(5):
    row = []
    for j in range(3):
        element = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix_5x3.append(row)

matrix_A = np.array(matrix_5x3)

print("\nEnter elements for 3×2 Matrix:")
print("-" * 70)
matrix_3x2 = []
for i in range(3):
    row = []
    for j in range(2):
        element = int(input(f"Enter element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix_3x2.append(row)

matrix_B = np.array(matrix_3x2)

print("\n" + "=" * 70)
print("Matrix A (5×3):")
print("-" * 70)
print(matrix_A)

print("\nMatrix B (3×2):")
print("-" * 70)
print(matrix_B)

product_matrix = np.matmul(matrix_A, matrix_B)

print("\nProduct Matrix (5×2) = A × B:")
print("-" * 70)
print(product_matrix)

print("\n" + "=" * 70)
