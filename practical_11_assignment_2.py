"""
================================================================================
Practical No: 11
Lab Assignment: 2
Title: Recruitment Analysis Visualization

AIM:
    To import dataset of new recruitments in companies and visualize using
    Bar Chart, Pie Chart, Customized Pie Chart, Doughnut Chart, and compare
    recruitments in specific companies.
================================================================================
"""

import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Cognizant', 'Amdocs']
recruitments = [120, 150, 135, 90, 110, 95, 80, 105, 85]

print("=" * 70)
print(" " * 18 + "RECRUITMENT ANALYSIS VISUALIZATION")
print("=" * 70)

plt.figure(figsize=(12, 6))
plt.bar(companies, recruitments, color='teal', edgecolor='black')
plt.xlabel('Companies')
plt.ylabel('Number of Recruitments')
plt.title('New Recruitments - Bar Chart')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('recruitment_bar_chart.png')
print("\n(a) Bar Chart saved as 'recruitment_bar_chart.png'")
plt.show()

plt.figure(figsize=(10, 8))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', startangle=90)
plt.title('New Recruitments Distribution - Pie Chart')
plt.tight_layout()
plt.savefig('recruitment_pie_chart.png')
print("(b) Pie Chart saved as 'recruitment_pie_chart.png'")
plt.show()

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ffccff']
explode = [0.1 if i == recruitments.index(max(recruitments)) else 0 for i in range(len(recruitments))]

plt.figure(figsize=(10, 8))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('New Recruitments Distribution - Customized Pie Chart')
plt.tight_layout()
plt.savefig('recruitment_custom_pie_chart.png')
print("(c) Customized Pie Chart saved as 'recruitment_custom_pie_chart.png'")
plt.show()

plt.figure(figsize=(10, 8))
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'width': 0.4})
circle = plt.Circle((0, 0), 0.6, color='white')
plt.gca().add_artist(circle)
plt.title('New Recruitments Distribution - Doughnut Chart')
plt.tight_layout()
plt.savefig('recruitment_doughnut_chart.png')
print("(d) Doughnut Chart saved as 'recruitment_doughnut_chart.png'")
plt.show()

ibm_index = companies.index('IBM')
amdocs_index = companies.index('Amdocs')
comparison_companies = ['IBM', 'Amdocs']
comparison_values = [recruitments[ibm_index], recruitments[amdocs_index]]

plt.figure(figsize=(8, 6))
bars = plt.bar(comparison_companies, comparison_values, color=['#ff6666', '#66b3ff'], edgecolor='black', width=0.5)
plt.xlabel('Companies')
plt.ylabel('Number of Recruitments')
plt.title('Comparison: IBM vs Amdocs Recruitments')
plt.ylim(0, max(comparison_values) + 20)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('ibm_amdocs_comparison.png')
print("(e) Comparison Chart saved as 'ibm_amdocs_comparison.png'")
plt.show()

print("\n" + "=" * 70)
print("All visualizations have been created and saved successfully!")
print("=" * 70)
