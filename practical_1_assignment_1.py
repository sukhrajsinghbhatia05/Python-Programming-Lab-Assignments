"""
================================================================================
Practical No: 1
Lab Assignment: 1
Title: Employee Salary Calculator

AIM:
    To create a Python program that calculates and displays the complete salary
    breakdown of an employee including allowances and deductions.
================================================================================
"""

print("=" * 60)
print(" " * 15 + "EMPLOYEE SALARY CALCULATOR")
print("=" * 60)

name = input("\nEnter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: Rs. "))

da = basic_salary * 0.92
hra = basic_salary * 0.58
ta = basic_salary * 0.30
lic = 500

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

print("\n" + "=" * 60)
print(" " * 20 + "SALARY SLIP")
print("=" * 60)
print(f"\nEmployee Name       : {name}")
print(f"Employee ID         : {emp_id}")
print(f"Department          : {department}")
print("-" * 60)
print(f"\nBasic Salary        : Rs. {basic_salary:.2f}")
print(f"DA (92%)            : Rs. {da:.2f}")
print(f"HRA (58%)           : Rs. {hra:.2f}")
print(f"TA (30%)            : Rs. {ta:.2f}")
print("-" * 60)
print(f"Gross Salary        : Rs. {gross_salary:.2f}")
print(f"LIC Deduction       : Rs. {lic:.2f}")
print("-" * 60)
print(f"NET SALARY          : Rs. {net_salary:.2f}")
print("=" * 60)
