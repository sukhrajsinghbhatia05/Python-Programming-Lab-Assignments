"""
================================================================================
Practical No: 6
Lab Assignment: 2
Title: Capitalize Lines Function

AIM:
    To design a function that accepts a sequence of lines as input and prints
    the lines after capitalizing all characters.
================================================================================
"""

def capitalize_lines(lines):
    print("\n" + "=" * 70)
    print(" " * 25 + "CAPITALIZED OUTPUT")
    print("=" * 70)
    
    for line in lines:
        print(line.upper())
    
    print("=" * 70)


print("=" * 70)
print(" " * 20 + "LINE CAPITALIZER PROGRAM")
print("=" * 70)

print("\nEnter lines of text (type 'END' on a new line to finish):")
print("-" * 70)

lines_list = []
while True:
    line = input()
    if line == 'END':
        break
    lines_list.append(line)

if len(lines_list) > 0:
    capitalize_lines(lines_list)
else:
    print("\nNo lines entered!")
