"""
================================================================================
Practical No: 3
Task: 4
Title: Descending Star Pattern

AIM:
    To construct a program that prints a descending star pattern from 5 stars
    to 1 star.
================================================================================
"""

print("Descending Star Pattern:\n")

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    
    for k in range(i):
        print("*", end=" ")
    
    print()
