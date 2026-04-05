"""
================================================================================
Practical No: 5
Lab Assignment: 2
Title: Shop Pricing System Using Tuples

AIM:
    To create a program that stores prices of sold items in a tuple and performs
    analysis including finding total, cheapest, costliest, and sorting.
================================================================================
"""

print("=" * 70)
print(" " * 18 + "SHOP PRICING ANALYSIS SYSTEM")
print("=" * 70)

print("\nEnter prices of sold items (type 'done' to finish):")
prices = []
while True:
    user_input = input("Enter price: Rs. ")
    if user_input.lower() == 'done':
        break
    try:
        prices.append(float(user_input))
    except ValueError:
        print("Invalid input! Please enter a valid price.")

price_tuple = tuple(prices)

print("\n" + "=" * 70)
print("SALES ANALYSIS REPORT")
print("=" * 70)

if len(price_tuple) == 0:
    print("\nNo items sold today!")
else:
    total_items = len(price_tuple)
    print(f"\n(a) Total number of items sold: {total_items}")
    
    cheapest_price = min(price_tuple)
    print(f"\n(b) Price of cheapest item sold: Rs. {cheapest_price:.2f}")
    
    costliest_price = max(price_tuple)
    print(f"\n(c) Price of costliest item sold: Rs. {costliest_price:.2f}")
    
    sorted_prices = sorted(price_tuple)
    print(f"\n(d) Price list in ascending order:")
    for i, price in enumerate(sorted_prices, 1):
        print(f"    {i}. Rs. {price:.2f}")
    
    costliest_count = price_tuple.count(costliest_price)
    print(f"\n(e) Number of costliest items (Rs. {costliest_price:.2f}) sold: {costliest_count}")

print("\n" + "=" * 70)
