"""
================================================================================
Practical No: 11
Lab Assignment: 1
Title: Cosmetic Sales Visualization

AIM:
    To import sales data of a Cosmetic Company and visualize it using
    Line Plot, Multiline Plot, Bar chart, and Pie chart.
================================================================================
"""

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
total_profit = [50000, 55000, 60000, 58000, 65000, 70000, 75000, 72000, 78000, 82000, 85000, 90000]
facecream_sales = [12000, 13000, 14000, 13500, 15000, 16000, 17000, 16500, 18000, 19000, 20000, 21000]
facewash_sales = [8000, 8500, 9000, 8800, 9500, 10000, 10500, 10200, 11000, 11500, 12000, 12500]

print("=" * 70)
print(" " * 18 + "COSMETIC SALES VISUALIZATION")
print("=" * 70)

plt.figure(figsize=(10, 6))
plt.plot(months, total_profit, marker='o', linewidth=2, color='blue')
plt.xlabel('Months')
plt.ylabel('Total Profit (Rs.)')
plt.title('Total Profit of All Months - Line Plot')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('profit_line_plot.png')
print("\n(a) Line Plot saved as 'profit_line_plot.png'")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(months, facecream_sales, marker='s', label='Face Cream', linewidth=2)
plt.plot(months, facewash_sales, marker='^', label='Face Wash', linewidth=2)
plt.xlabel('Months')
plt.ylabel('Sales (Rs.)')
plt.title('Product Sales Data - Multiline Plot')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('products_multiline_plot.png')
print("(b) Multiline Plot saved as 'products_multiline_plot.png'")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, facecream_sales, color='skyblue', label='Face Cream')
plt.bar(months, facewash_sales, bottom=facecream_sales, color='lightcoral', label='Face Wash')
plt.xlabel('Months')
plt.ylabel('Sales (Rs.)')
plt.title('Face Cream and Face Wash Sales - Bar Chart')
plt.legend()
plt.tight_layout()
plt.savefig('products_bar_chart.png')
print("(c) Bar Chart saved as 'products_bar_chart.png'")
plt.show()

products = ['Face Cream', 'Face Wash', 'Shampoo', 'Moisturizer']
last_year_sales = [250000, 150000, 180000, 120000]

plt.figure(figsize=(8, 8))
plt.pie(last_year_sales, labels=products, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Total Sale Data for Last Year - Pie Chart')
plt.tight_layout()
plt.savefig('sales_pie_chart.png')
print("(d) Pie Chart saved as 'sales_pie_chart.png'")
plt.show()

print("\n" + "=" * 70)
print("All visualizations have been created and saved successfully!")
print("=" * 70)
