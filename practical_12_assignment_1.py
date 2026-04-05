"""
================================================================================
Practical No: 12
Lab Assignment: 1
Title: Diamonds DataFrame Analysis

AIM:
    To perform statistical analysis on diamonds dataset including calculating
    mean price for each cut, finding count/min/max prices for each cut, and
    calculating average values for x, y, and z parameters separately.
================================================================================
"""

import pandas as pd

diamonds_data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(diamonds_data)

print("=" * 90)
print(" " * 30 + "DIAMONDS ANALYSIS")
print("=" * 90)

print("\nOriginal Diamonds DataFrame:")
print("-" * 90)
print(df.to_string(index=False))

print("\n(i) Mean of price for each cut of diamonds:")
print("-" * 90)
mean_price_by_cut = df.groupby('cut')['price'].mean()
print(mean_price_by_cut)

print("\n(ii) Count, minimum and maximum price for each cut of diamonds:")
print("-" * 90)
price_stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print(price_stats)

print("\n(iii) Average value of parameter x, y, and z separately:")
print("-" * 90)
avg_x = df['x'].mean()
avg_y = df['y'].mean()
avg_z = df['z'].mean()
print(f"Average x: {avg_x:.2f}")
print(f"Average y: {avg_y:.2f}")
print(f"Average z: {avg_z:.2f}")

print("\n" + "=" * 90)
