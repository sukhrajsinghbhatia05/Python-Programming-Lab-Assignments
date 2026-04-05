"""
================================================================================
Practical No: 7
Lab Assignment: 1
Title: Menu-Driven Calculator

AIM:
    To create a menu-driven application implementing different functions for
    basic arithmetic operations: Addition, Subtraction, Multiplication,
    Division, and Modulus.
================================================================================
"""

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero!"
    return a % b


print("=" * 60)
print(" " * 20 + "CALCULATOR")
print("=" * 60)

while True:
    print("\nMENU:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '6':
        print("\nThank you for using the calculator!")
        break
    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = addition(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtraction(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiplication(num1, num2)
            print(f"\nResult: {num1} × {num2} = {result}")
        elif choice == '4':
            result = division(num1, num2)
            print(f"\nResult: {num1} ÷ {num2} = {result}")
        elif choice == '5':
            result = modulus(num1, num2)
            print(f"\nResult: {num1} % {num2} = {result}")
    else:
        print("\nInvalid choice! Please try again.")
    
    print("-" * 60)
