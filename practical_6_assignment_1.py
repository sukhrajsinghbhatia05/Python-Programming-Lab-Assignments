"""
================================================================================
Practical No: 6
Lab Assignment: 1
Title: String Statistics Calculator

AIM:
    To develop an application that analyzes a string and prints statistics
    including vowels, consonants, spaces, and lowercase letters.
================================================================================
"""

print("=" * 70)
print(" " * 20 + "STRING STATISTICS CALCULATOR")
print("=" * 70)

user_string = input("\nEnter a string: ")

vowels = 0
consonants = 0
spaces = 0
lowercase_letters = 0

vowel_list = "aeiouAEIOU"

for char in user_string:
    if char.isalpha():
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
        
        if char.islower():
            lowercase_letters += 1
    elif char == ' ':
        spaces += 1

print("\n" + "=" * 70)
print(" " * 25 + "STATISTICS")
print("=" * 70)
print(f"\n(a) Number of Vowels           : {vowels}")
print(f"(b) Number of Consonants       : {consonants}")
print(f"(c) Number of Spaces           : {spaces}")
print(f"(d) Number of Lowercase Letters: {lowercase_letters}")
print("\n" + "=" * 70)
