"""
================================================================================
Practical No: 10
Lab Assignment: 2
Title: States Analysis with Population Density

AIM:
    To create a table with information about 5 states including name, area, and
    population. Generate reports showing complete information, state with largest
    area/population, and calculate population density.
================================================================================
"""

import pandas as pd

states_data = {
    'State': ['Maharashtra', 'Uttar Pradesh', 'Karnataka', 'Tamil Nadu', 'Rajasthan'],
    'Area': [307713, 240928, 191791, 130060, 342239],
    'Population': [112374333, 199812341, 61095297, 72147030, 68548437]
}

df = pd.DataFrame(states_data)

df['Population_Density'] = df['Population'] / df['Area']

print("=" * 80)
print(" " * 25 + "STATES ANALYSIS")
print("=" * 80)

print("\n(a) Complete information of states:")
print("-" * 80)
print(df.to_string(index=False))

largest_area_state = df.loc[df['Area'].idxmax()]
print(f"\n(b) Name of State having largest Area:")
print("-" * 80)
print(f"{largest_area_state['State']} (Area: {largest_area_state['Area']} sq km)")

largest_pop_state = df.loc[df['Population'].idxmax()]
print(f"\n(c) Name of State having largest population:")
print("-" * 80)
print(f"{largest_pop_state['State']} (Population: {largest_pop_state['Population']})")

print("\n(d) Population density of States:")
print("-" * 80)
for index, row in df.iterrows():
    print(f"{row['State']:20s}: {row['Population_Density']:.2f} people/sq km")

highest_density_state = df.loc[df['Population_Density'].idxmax()]
print(f"\n(e) Name of State with highest population density:")
print("-" * 80)
print(f"{highest_density_state['State']} (Density: {highest_density_state['Population_Density']:.2f} people/sq km)")

highest_pop_density_state = df.loc[df['Population_Density'].idxmax()]
print(f"\n(f) Name of State with highest population density:")
print("-" * 80)
print(f"{highest_pop_density_state['State']} (Density: {highest_pop_density_state['Population_Density']:.2f} people/sq km)")

print("\n" + "=" * 80)
