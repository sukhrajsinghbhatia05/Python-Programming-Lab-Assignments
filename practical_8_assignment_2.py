"""
================================================================================
Practical No: 8
Lab Assignment: 2
Title: Copy Python Script Without Comments

AIM:
    To develop an application using file handling to copy the contents of a
    python script into another file without including the comments.
================================================================================
"""

print("=" * 70)
print(" " * 15 + "PYTHON SCRIPT COPIER (NO COMMENTS)")
print("=" * 70)

source_file = input("\nEnter source Python file name (e.g., source.py): ")
destination_file = input("Enter destination file name (e.g., destination.py): ")

try:
    with open(source_file, 'r') as src:
        lines = src.readlines()
    
    with open(destination_file, 'w') as dest:
        for line in lines:
            stripped_line = line.strip()
            
            if stripped_line.startswith('#'):
                continue
            
            if '#' in line:
                code_part = line.split('#')[0]
                if code_part.strip():
                    dest.write(code_part.rstrip() + '\n')
            else:
                dest.write(line)
    
    print(f"\nSuccess! Python script copied without comments.")
    print(f"Output saved to: {destination_file}")
    
except FileNotFoundError:
    print(f"\nError: File '{source_file}' not found!")
except Exception as e:
    print(f"\nAn error occurred: {e}")

print("\n" + "=" * 70)
