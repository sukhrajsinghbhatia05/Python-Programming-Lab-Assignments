"""
================================================================================
Practical No: 3
Task: 7
Title: Prime Number Finder

AIM:
    To write a program that finds and prints all prime numbers between two
    numbers entered by the user using loops.
================================================================================
"""

print("=" * 60)
print(" " * 18 + "PRIME NUMBER FINDER")
print("=" * 60)

while True:
    start = int(input("\nEnter the starting number: "))
    end = int(input("Enter the ending number: "))
    
    if start < 1 or end < 1:
        print("Please enter positive numbers!")
        continue
    if start > end:
        print("Starting number should be less than or equal to ending number!")
        continue
    break

print(f"\nPrime numbers between {start} and {end}:")
print("-" * 60)

prime_count = 0

for num in range(start, end + 1):
    if num < 2:
        continue
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end="  ")
        prime_count += 1
        if prime_count % 10 == 0:
            print()

print(f"\n\nTotal prime numbers found: {prime_count}")
print("=" * 60)
