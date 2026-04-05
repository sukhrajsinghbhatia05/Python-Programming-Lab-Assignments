"""
================================================================================
Practical No: 3
Task: 1
Title: Number Patterns

AIM:
    To construct programs that print various number patterns as shown in the
    practical manual.
================================================================================
"""

print("Pattern 1:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern 2:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()

print("\nPattern 3:")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPattern 4:")
for i in range(1, 6):
    num = i
    for j in range(i):
        print(num, end="")
        num += i
    print()

print("\nPattern 5:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\nPattern 6 (Binary):")
for i in range(1, 6):
    for j in range(i):
        print(i % 2, end=" ")
    print()

print("\nPattern 7 (Even numbers):")
num = 2
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
