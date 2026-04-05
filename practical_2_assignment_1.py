"""
================================================================================
Practical No: 2
Lab Assignment: 1
Title: Ohm's Law Calculator with Current Classification

AIM:
    To develop a Python program that calculates current using Ohm's Law and
    classifies the current as Low, Normal, or High.
================================================================================
"""

print("=" * 60)
print(" " * 15 + "OHM'S LAW CALCULATOR")
print("=" * 60)

voltage = float(input("\nEnter Voltage (V) in Volts: "))
resistance = float(input("Enter Resistance (R) in Ohms: "))

if resistance == 0:
    print("\nError: Resistance cannot be zero!")
else:
    current = voltage / resistance
    
    print("\n" + "-" * 60)
    print(f"Voltage (V)       : {voltage} V")
    print(f"Resistance (R)    : {resistance} Ω")
    print(f"Current (I)       : {current:.4f} A")
    print("-" * 60)
    
    print("\nCurrent Classification:")
    if current < 0.5:
        print("Status: Low current")
    elif current <= 2:
        print("Status: Normal current")
    else:
        print("Status: High current")
    
    print("=" * 60)
