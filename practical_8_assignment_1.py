"""
================================================================================
Practical No: 8
Lab Assignment: 1
Title: Text File to Uppercase Converter

AIM:
    To construct a program that reads a text file and writes its contents into
    a new text file with the same content but in uppercase.
================================================================================
"""

print("=" * 70)
print(" " * 18 + "TEXT FILE TO UPPERCASE CONVERTER")
print("=" * 70)

input_filename = input("\nEnter the input filename (e.g., input.txt): ")
output_filename = input("Enter the output filename (e.g., output.txt): ")

try:
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
    
    uppercase_content = content.upper()
    
    with open(output_filename, 'w') as output_file:
        output_file.write(uppercase_content)
    
    print(f"\nSuccess! Content has been converted to uppercase.")
    print(f"Output saved to: {output_filename}")
    
except FileNotFoundError:
    print(f"\nError: File '{input_filename}' not found!")
except Exception as e:
    print(f"\nAn error occurred: {e}")

print("\n" + "=" * 70)
