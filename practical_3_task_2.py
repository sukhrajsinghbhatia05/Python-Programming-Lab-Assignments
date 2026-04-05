"""
================================================================================
Practical No: 3
Task: 2
Title: Character and Symbol Patterns

AIM:
    To construct programs that print various character and symbol patterns.
================================================================================
"""

print("Pattern 1 (A, AB, ABC...):")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\nPattern 2 (*, * #, * # *...):")
for i in range(1, 6):
    for j in range(i):
        if j % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()

print("\nPattern 3 (P, PP, PPP...):")
for i in range(1, 6):
    for j in range(i):
        print("P", end="")
    print()

print("\nPattern 4 (p, py, pyt, pyth, pytho, python):")
word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])

print("\nPattern 5 (aaaaa, bbbb, ccc, dd, e):")
for i in range(5, 0, -1):
    char = chr(65 + (5 - i))
    for j in range(i):
        print(char.lower(), end="")
    print()
