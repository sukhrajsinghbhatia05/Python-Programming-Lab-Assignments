"""
================================================================================
Practical No: 5
Lab Assignment: 1
Title: Comprehensive Tuple Operations

AIM:
    To develop a program that performs various operations on tuples including
    counting items, printing last item, reversing, searching, and sorting.
================================================================================
"""

print("=" * 70)
print(" " * 20 + "TUPLE OPERATIONS")
print("=" * 70)

print("\nEnter integers (type 'done' to finish):")
numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input! Please enter a number or 'done'.")

my_tuple = tuple(numbers)

print("\n" + "=" * 70)
print(f"Original Tuple: {my_tuple}")
print("=" * 70)

print(f"\n(a) Total number of items in the Tuple: {len(my_tuple)}")

if len(my_tuple) > 0:
    print(f"\n(b) Last item in the Tuple: {my_tuple[-1]}")
else:
    print("\n(b) Tuple is empty!")

print(f"\n(c) Tuple elements in reverse order: {my_tuple[::-1]}")

search_item = int(input("\n(d) Enter a number to search in the tuple: "))
if search_item in my_tuple:
    print("Yes")
else:
    print("No")

if len(my_tuple) > 2:
    remaining = list(my_tuple[1:-1])
    remaining.sort()
    print(f"\n(e) After removing first and last items and sorting: {remaining}")
elif len(my_tuple) <= 2:
    print("\n(e) Not enough items to remove first and last!")

print("\n" + "=" * 70)
