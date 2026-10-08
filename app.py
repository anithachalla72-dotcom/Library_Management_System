import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="library_db"
)

print("Database connected successfully!")
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))

    cursor = db.cursor()

    query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
    values = (title, author, quantity)

    cursor.execute(query, values)
    db.commit()

    print("Book added successfully!")


def view_books():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\n--- Books in Library ---")

    for book in books:
        print(book)
def search_book():
    title = input("Enter book title to search: ")

    cursor = db.cursor()

    query = "SELECT * FROM books WHERE title LIKE %s"
    value = ("%" + title + "%",)

    cursor.execute(query, value)
    books = cursor.fetchall()

    if books:
        print("\n--- Search Results ---")
        for book in books:
            print(book)
    else:
        print("Book not found!")

def add_member():
    name = input("Enter member name: ")
    department = input("Enter department: ")

    cursor = db.cursor()

    query = "INSERT INTO members (name, department) VALUES (%s, %s)"
    values = (name, department)

    cursor.execute(query, values)
    db.commit()

    print("Member added successfully!")

def view_members():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    print("\n--- Library Members ---")

    for member in members:
        print(member)

def issue_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))

    cursor = db.cursor()

    query = """
    INSERT INTO issued_books (book_id, member_id, issue_date)
    VALUES (%s, %s, CURDATE())
    """

    cursor.execute(query, (book_id, member_id))
    db.commit()

    print("Book issued successfully!")
def view_issued_books():
    cursor = db.cursor()

    query = """
    SELECT issued_books.issue_id,
           books.title,
           members.name,
           issued_books.issue_date,
           issued_books.return_date
    FROM issued_books
    JOIN books ON issued_books.book_id = books.book_id
    JOIN members ON issued_books.member_id = members.member_id
    """

    cursor.execute(query)
    records = cursor.fetchall()

    print("\n--- Issued Books ---")

    for record in records:
        print(record)
def return_book():
    issue_id = int(input("Enter issue ID: "))

    cursor = db.cursor()

    query = """
    UPDATE issued_books
    SET return_date = CURDATE()
    WHERE issue_id = %s
    """

    cursor.execute(query, (issue_id,))
    db.commit()

    print("Book returned successfully!")
def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    cursor = db.cursor()

    query = "DELETE FROM books WHERE book_id = %s"
    cursor.execute(query, (book_id,))
    db.commit()

    print("Book deleted successfully!")
def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    cursor = db.cursor()

    query = "DELETE FROM books WHERE book_id = %s"
    cursor.execute(query, (book_id,))
    db.commit()

    print("Book deleted successfully!")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Member")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View Issued Books")
    print("9. Delete Book")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        add_member()

    elif choice == "5":
        view_members()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        view_issued_books()

    elif choice == "9":
        delete_book()

    elif choice == "10":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice!")
