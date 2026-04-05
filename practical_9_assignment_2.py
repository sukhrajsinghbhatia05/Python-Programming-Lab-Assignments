"""
================================================================================
Practical No: 9
Lab Assignment: 2
Title: Library Management System

AIM:
    To create a Library Management System with classes for Book, Member, and
    Library. Implement methods for adding books, lending books to members,
    returning books, and displaying book information with a menu-driven interface.
================================================================================
"""

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True
    
    def display_info(self):
        status = "Available" if self.is_available else "Issued"
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")
    
    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered successfully!")
    
    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        
        if not book:
            print("Book not found!")
            return
        if not member:
            print("Member not found!")
            return
        if not book.is_available:
            print("Book is already issued!")
            return
        
        book.is_available = False
        member.borrowed_books.append(book)
        print(f"Book '{book.title}' issued to {member.name}")
    
    def return_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        
        if not book or not member:
            print("Invalid book ID or member ID!")
            return
        
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned successfully!")
        else:
            print("This book was not borrowed by this member!")
    
    def display_books(self):
        if not self.books:
            print("No books in the library!")
            return
        print("\n" + "=" * 80)
        print(" " * 30 + "BOOKS IN LIBRARY")
        print("=" * 80)
        for book in self.books:
            book.display_info()
        print("=" * 80)


library = Library()

print("=" * 70)
print(" " * 18 + "LIBRARY MANAGEMENT SYSTEM")
print("=" * 70)

while True:
    print("\nMENU:")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book_id = input("Enter book ID: ")
        library.add_book(Book(title, author, book_id))
    
    elif choice == '2':
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        library.add_member(Member(name, member_id))
    
    elif choice == '3':
        book_id = input("Enter book ID to lend: ")
        member_id = input("Enter member ID: ")
        library.lend_book(book_id, member_id)
    
    elif choice == '4':
        book_id = input("Enter book ID to return: ")
        member_id = input("Enter member ID: ")
        library.return_book(book_id, member_id)
    
    elif choice == '5':
        library.display_books()
    
    elif choice == '6':
        print("\nThank you for using the Library Management System!")
        break
    
    else:
        print("Invalid choice! Please try again.")
    
    print("-" * 70)
