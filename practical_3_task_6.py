"""
================================================================================
Practical No: 3
Task: 6
Title: Reverse Pyramid Star Pattern

AIM:
    To write a program that prints a reverse pyramid (inverted triangle)
    star pattern using for loop.
================================================================================
"""

print("Reverse Pyramid Star Pattern:\n")

rows = 5

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    
    for k in range(2 * i - 1):
        print("*", end=" ")
    
    print()
