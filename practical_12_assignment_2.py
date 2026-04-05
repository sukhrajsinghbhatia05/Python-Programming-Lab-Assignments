"""
================================================================================
Practical No: 12
Lab Assignment: 2
Title: Employee Excel Analysis

AIM:
    To read employee.xlsx file and construct programs to print reports:
    employees working for Automotive domain, employee details with given ID,
    and list of all Developers at Infosys.
================================================================================
"""

import pandas as pd

employee_data = {
    'Employee_ID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008'],
    'Employee_Name': ['Rahul Sharma', 'Priya Singh', 'Amit Kumar', 'Sneha Patel', 'Vikram Rao', 'Anjali Verma', 'Rohan Gupta', 'Neha Joshi'],
    'Department': ['Automotive', 'IT', 'Automotive', 'Finance', 'IT', 'Automotive', 'IT', 'HR'],
    'Designation': ['Engineer', 'Developer', 'Manager', 'Analyst', 'Developer', 'Developer', 'Developer', 'Manager'],
    'Company': ['Tata Motors', 'Infosys', 'Mahindra', 'HDFC', 'Infosys', 'Maruti', 'Infosys', 'TCS']
}

df = pd.DataFrame(employee_data)

df.to_excel('employee.xlsx', index=False)

print("=" * 90)
print(" " * 25 + "EMPLOYEE EXCEL ANALYSIS")
print("=" * 90)

df = pd.read_excel('employee.xlsx')

print("\n(a) Employees working for 'Automotive' domain:")
print("-" * 90)
automotive_employees = df[df['Department'] == 'Automotive']
if not automotive_employees.empty:
    print(automotive_employees.to_string(index=False))
else:
    print("No employees found in Automotive domain")

employee_id = input("\n\n(b) Enter Employee ID to search: ")
print(f"\nDetails of employee with ID {employee_id}:")
print("-" * 90)
employee_details = df[df['Employee_ID'] == employee_id]
if not employee_details.empty:
    print(employee_details.to_string(index=False))
else:
    print(f"No employee found with ID {employee_id}")

print("\n(c) List of all Developers at Infosys:")
print("-" * 90)
infosys_developers = df[(df['Designation'] == 'Developer') & (df['Company'] == 'Infosys')]
if not infosys_developers.empty:
    print(infosys_developers.to_string(index=False))
else:
    print("No developers found at Infosys")

print("\n" + "=" * 90)
