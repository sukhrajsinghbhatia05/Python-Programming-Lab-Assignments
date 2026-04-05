"""
================================================================================
Practical No: 9
Lab Assignment: 1
Title: Employee-Manager System using Inheritance

AIM:
    To create a class Employee and inherit it into another class Manager.
    Add methods to get input and print information of employees for 10 managers.
================================================================================
"""

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""
    
    def get_input(self):
        self.name = input("  Enter Name: ")
        self.age = int(input("  Enter Age: "))
        self.salary = float(input("  Enter Salary: Rs. "))
        self.address = input("  Enter Address: ")
    
    def display(self):
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")
        print(f"  Salary  : Rs. {self.salary:.2f}")
        print(f"  Address : {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
    
    def get_manager_input(self):
        self.get_input()
    
    def display_manager(self):
        self.display()


print("=" * 70)
print(" " * 18 + "EMPLOYEE-MANAGER SYSTEM")
print("=" * 70)

managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}:")
    print("-" * 70)
    mgr = Manager()
    mgr.get_manager_input()
    managers.append(mgr)

print("\n" + "=" * 70)
print(" " * 20 + "MANAGER INFORMATION")
print("=" * 70)

for i, mgr in enumerate(managers, 1):
    print(f"\nManager {i}:")
    print("-" * 70)
    mgr.display_manager()

print("\n" + "=" * 70)
