"""
================================================================================
Practical No: 3
Task: 3
Title: Print Consecutive Numbers Without String Methods

AIM:
    To print consecutive numbers from 1 to n as a single string without using
    any string methods.
================================================================================
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i, end='')

print()
