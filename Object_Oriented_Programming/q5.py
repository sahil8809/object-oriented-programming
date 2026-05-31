

class Library:   # a class called Library
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added successfully!")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("Available Books:")
            for b in self.books:
                print("-", b)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued successfully!")
        else:
            print("Book not available!")

    def return_book(self, book):
        self.books.append(book)
        print(f"{book} returned successfully!")


# 🔷 Object
lib = Library()

# 🔷 Menu
while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        b = input("Enter book name: ")
        lib.add_book(b)

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        b = input("Enter book to issue: ")
        lib.issue_book(b)

    elif choice == "4":
        b = input("Enter book to return: ")
        lib.return_book(b)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
