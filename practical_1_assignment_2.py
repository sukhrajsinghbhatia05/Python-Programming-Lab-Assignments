"""
================================================================================
Practical No: 1
Lab Assignment: 2
Title: Vendor Billing System

AIM:
    To create a Python program that stores vendor details and generates an
    annual purchase/billing report based on monthly purchase data.
================================================================================
"""

print("=" * 70)
print(" " * 20 + "VENDOR BILLING SYSTEM")
print("=" * 70)

vendor_name = input("\nEnter Vendor Name: ")
year_of_association = input("Enter Year of Association: ")
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

monthly_purchases = []
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print("\n" + "-" * 70)
print("Enter Monthly Purchase Amounts:")
print("-" * 70)

for i in range(12):
    purchase = float(input(f"{months[i]:12s}: Rs. "))
    monthly_purchases.append(purchase)

total_annual_purchase = sum(monthly_purchases)
average_monthly_purchase = total_annual_purchase / 12

print("\n" + "=" * 70)
print(" " * 18 + "ANNUAL PURCHASE/BILLING REPORT")
print("=" * 70)
print(f"\nVendor Name            : {vendor_name}")
print(f"Year of Association    : {year_of_association}")
print(f"Contact Number         : {contact_number}")
print(f"Email ID               : {email_id}")
print("\n" + "-" * 70)
print(" " * 20 + "MONTHLY PURCHASE DETAILS")
print("-" * 70)

for i in range(12):
    print(f"{months[i]:12s}       : Rs. {monthly_purchases[i]:10.2f}")

print("-" * 70)
print(f"\nTotal Annual Purchase  : Rs. {total_annual_purchase:.2f}")
print(f"Average Monthly Purchase: Rs. {average_monthly_purchase:.2f}")
print("=" * 70)
