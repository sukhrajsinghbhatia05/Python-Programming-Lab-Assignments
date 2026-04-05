"""
================================================================================
Practical No: 10
Lab Assignment: 1
Title: Books Analysis Using Pandas

AIM:
    To create a Pandas DataFrame from books.csv and perform various operations
    including tabular display, filtering by author and publisher, finding
    cheapest/costliest books, and sorting by year.
================================================================================
"""

import pandas as pd

books_data = {
    'Title': ['Python Basics', 'Data Science', 'Machine Learning', 'Web Development', 'AI Fundamentals'],
    'Author': ['John Smith', 'Jane Doe', 'John Smith', 'Bob Wilson', 'Jane Doe'],
    'Edition': ['3rd', '2nd', '1st', '4th', '2nd'],
    'Publication_Year': [2020, 2019, 2021, 2018, 2022],
    'Publisher': ['TechBooks', 'DataPub', 'TechBooks', 'WebPress', 'DataPub'],
    'Price': [450, 680, 720, 520, 890]
}

df = pd.DataFrame(books_data)

df.to_csv('books.csv', index=False)

print("=" * 90)
print(" " * 30 + "BOOKS ANALYSIS")
print("=" * 90)

print("\n(a) Complete record of books in Tabular form:")
print("-" * 90)
print(df.to_string(index=False))

author_name = input("\n\nEnter author name to filter: ")
print(f"\n(b) List of available books of author '{author_name}':")
print("-" * 90)
author_books = df[df['Author'] == author_name]
if not author_books.empty:
    print(author_books.to_string(index=False))
else:
    print(f"No books found by {author_name}")

publisher_name = input("\n\nEnter publishing house name to filter: ")
print(f"\n(c) List of available books of publishing house '{publisher_name}':")
print("-" * 90)
publisher_books = df[df['Publisher'] == publisher_name]
if not publisher_books.empty:
    print(publisher_books.to_string(index=False))
else:
    print(f"No books found from {publisher_name}")

print("\n(d) Titles of cheapest and costliest book available:")
print("-" * 90)
cheapest = df.loc[df['Price'].idxmin()]
costliest = df.loc[df['Price'].idxmax()]
print(f"Cheapest: {cheapest['Title']} (Rs. {cheapest['Price']})")
print(f"Costliest: {costliest['Title']} (Rs. {costliest['Price']})")

print("\n(e) List sorted by year of publication:")
print("-" * 90)
sorted_df = df.sort_values('Publication_Year')
print(sorted_df.to_string(index=False))

print("\n" + "=" * 90)
