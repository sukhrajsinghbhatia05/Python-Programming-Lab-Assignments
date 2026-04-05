"""
================================================================================
Practical No: 7
Lab Assignment: 2
Title: Bank Account System

AIM:
    To create a menu-driven program for showing details of a Bank Account by
    implementing functions for displaying balance, depositing, and withdrawing.
================================================================================
"""

balance = 10000.00

def display_balance():
    print(f"\nCurrent Balance: Rs. {balance:.2f}")

def deposit():
    global balance
    amount = float(input("\nEnter amount to deposit: Rs. "))
    if amount > 0:
        balance += amount
        print(f"Rs. {amount:.2f} deposited successfully!")
        print(f"New Balance: Rs. {balance:.2f}")
    else:
        print("Invalid amount! Please enter a positive value.")

def withdraw():
    global balance
    amount = float(input("\nEnter amount to withdraw: Rs. "))
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully!")
            print(f"Remaining Balance: Rs. {balance:.2f}")
        else:
            print("Insufficient balance!")
    else:
        print("Invalid amount! Please enter a positive value.")


print("=" * 60)
print(" " * 18 + "BANK ACCOUNT SYSTEM")
print("=" * 60)

while True:
    print("\nMENU:")
    print("1. Display Current Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        display_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("\nThank you for using our banking system!")
        break
    else:
        print("\nInvalid choice! Please try again.")
    
    print("-" * 60)
