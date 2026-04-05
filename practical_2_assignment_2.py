"""
================================================================================
Practical No: 2
Lab Assignment: 2
Title: Steel Quality Grading System

AIM:
    To construct a program that grades steel quality based on hardness,
    carbon content, and tensile strength according to specified conditions.
================================================================================
"""

print("=" * 60)
print(" " * 15 + "STEEL QUALITY GRADING SYSTEM")
print("=" * 60)

hardness = float(input("\nEnter Hardness: "))
carbon_content = float(input("Enter Carbon Content: "))
tensile_strength = float(input("Enter Tensile Strength: "))

condition1 = hardness > 50
condition2 = carbon_content < 0.7
condition3 = tensile_strength > 5600

conditions_met = sum([condition1, condition2, condition3])

if condition1 and condition2 and condition3:
    grade = 10
    reason = "All three conditions are met"
elif condition1 and condition2:
    grade = 9
    reason = "Hardness > 50 and Carbon content < 0.7"
elif condition2 and condition3:
    grade = 8
    reason = "Carbon content < 0.7 and Tensile strength > 5600"
elif condition1 and condition3:
    grade = 7
    reason = "Hardness > 50 and Tensile strength > 5600"
elif conditions_met == 1:
    grade = 6
    reason = "Only one condition is met"
else:
    grade = 5
    reason = "None of the conditions are met"

print("\n" + "=" * 60)
print(" " * 20 + "GRADING RESULT")
print("=" * 60)
print(f"\nHardness           : {hardness}")
print(f"Carbon Content     : {carbon_content}")
print(f"Tensile Strength   : {tensile_strength}")
print("-" * 60)
print(f"\nCondition 1 (Hardness > 50)          : {'Met' if condition1 else 'Not Met'}")
print(f"Condition 2 (Carbon < 0.7)           : {'Met' if condition2 else 'Not Met'}")
print(f"Condition 3 (Tensile Strength > 5600): {'Met' if condition3 else 'Not Met'}")
print("-" * 60)
print(f"\nSTEEL GRADE: {grade}")
print(f"Reason: {reason}")
print("=" * 60)
