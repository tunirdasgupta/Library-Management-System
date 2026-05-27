import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Establish database connection
connection = None
cursor = None

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='ryan@2403',
                                         database='library_db')
    if connection.is_connected():
        cursor = connection.cursor()
        # Connection successful
except Error as e:
    print('Error while connecting to MySQL', e)
    exit()

# Admin login function
def admin_login():
    print("Enter admin credentials:")
    username = input("Username: ")
    password = input("Password: ")
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("Admin login successful!")
        return True
    else:
        print("Invalid admin username or password.")
        return False

# User login function
def user_login():
    print("Enter user credentials:")
    user_id = input("User ID: ")
    password = input("Password: ")
    query = "SELECT * FROM users WHERE user_id = %s AND password = %s"
    cursor.execute(query, (user_id, password))
    result = cursor.fetchone()
    if result:
        print("User login successful!")
        return result
    else:
        print("Invalid user ID or password.")
        return None

# Function to add a new user
def add_user():
    print("\nAdd New User")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    password = input("Enter Password: ")
    query = "INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)"
    values = (name, email, phone, password)
    cursor.execute(query, values)
    connection.commit()
    print("User added successfully with ID", cursor.lastrowid)

# Function to display all users
def display_users():
    print("\nList of Users:")
    cursor.execute("SELECT user_id, name, email, phone FROM users")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("ID:", row[0], "Name:", row[1], "Email:", row[2], "Phone:", row[3])
    else:
        print("No users found.")

# Function to update a user
def update_user():
    user_id = input("Enter User ID to update: ")
    print("Enter new data (leave blank to keep unchanged):")
    new_name = input("New Name: ")
    new_email = input("New Email: ")
    new_phone = input("New Phone: ")
    new_password = input("New Password: ")

    query = "SELECT name, email, phone, password FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    if not user:
        print("User ID not found.")
        return

    name_val = new_name if new_name else user[0]
    email_val = new_email if new_email else user[1]
    phone_val = new_phone if new_phone else user[2]
    password_val = new_password if new_password else user[3]

    update_query = "UPDATE users SET name=%s, email=%s, phone=%s, password=%s WHERE user_id=%s"
    cursor.execute(update_query, (name_val, email_val, phone_val, password_val, user_id))
    connection.commit()
    print("User updated successfully.")

# Function to delete a user
def delete_user():
    user_id = input("Enter User ID to delete: ")
    #Check if the user exists or not
    cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    if not user:
        print("User ID not found.")
        return
    
    confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        connection.commit()
        print("User deleted successfully.")
    else:
        print("Deletion cancelled.")

# Function to search for a user
def search_user():
    search_term = input("Enter user name or ID to search: ")
    if search_term.isdigit():
        cursor.execute("SELECT user_id, name, email, phone FROM users WHERE user_id = %s", (search_term,))
    else:
        cursor.execute("SELECT user_id, name, email, phone FROM users WHERE name LIKE %s", ('%' + search_term + '%',))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("ID:", row[0], "Name:", row[1], "Email:", row[2], "Phone:", row[3])
    else:
        print("No matching users found.")

# Function to add a new book
def add_book():
    print("\nAdd New Book")
    title = input("Title: ")
    author = input("Author: ")
    publisher = input("Publisher: ")
    year = input("Publication Year: ")
    copies = input("Number of copies: ")
    query = "INSERT INTO books (title, author, publisher, year, copies) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author, publisher, year, copies)
    cursor.execute(query, values)
    connection.commit()
    print("Book added successfully with ID", cursor.lastrowid)

# Function to display all books
def display_books():
    print("\nList of Books:")
    cursor.execute("SELECT book_id, title, author, year, copies FROM books")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("ID:", row[0], "Title:", row[1], "Author:", row[2], "Year:", row[3], "Copies:", row[4])
    else:
        print("No books found.")

# Function to update a book
def update_book():
    book_id = input("Enter Book ID to update: ")
    print("Enter new data (leave blank to keep unchanged):")
    new_title = input("New Title: ")
    new_author = input("New Author: ")
    new_publisher = input("New Publisher: ")
    new_year = input("New Year: ")
    new_copies = input("New Copies: ")

    query = "SELECT title, author, publisher, year, copies FROM books WHERE book_id = %s"
    cursor.execute(query, (book_id,))
    book = cursor.fetchone()
    if not book:
        print("Book ID not found.")
        return

    title_val = new_title if new_title else book[0]
    author_val = new_author if new_author else book[1]
    publisher_val = new_publisher if new_publisher else book[2]
    year_val = new_year if new_year else book[3]
    copies_val = new_copies if new_copies else book[4]

    update_query = "UPDATE books SET title=%s, author=%s, publisher=%s, year=%s, copies=%s WHERE book_id=%s"
    cursor.execute(update_query, (title_val, author_val, publisher_val, year_val, copies_val, book_id))
    connection.commit()
    print("Book updated successfully.")

# Function to delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    #check if book exists
    query = "SELECT book_id FROM books WHERE book_id = %s"
    cursor.execute(query, (book_id,))
    book = cursor.fetchone()
    if not book:
        print("Book ID not found.")
        return
    
    confirm = input(f"Are you sure you want to delete book {book_id}? (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        connection.commit()
        print("Book deleted successfully.")
    else:
        print("Deletion cancelled.")

# Function to search for a book
def search_book():
    search_term = input("Enter book title or ID to search: ")
    if search_term.isdigit():
        cursor.execute("SELECT book_id, title, author, year, copies FROM books WHERE book_id = %s", (search_term,))
    else:
        cursor.execute("SELECT book_id, title, author, year, copies FROM books WHERE title LIKE %s", ('%' + search_term + '%',))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("ID:", row[0], "Title:", row[1], "Author:", row[2], "Year:", row[3], "Copies:", row[4])
    else:
        print("No matching books found.")

# Function to issue a book to a user
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    user_id = input("Enter User ID: ")

    cursor.execute("SELECT copies FROM books WHERE book_id = %s", (book_id,))
    book = cursor.fetchone()
    if not book:
        print("Book not found.")
        return
    available_copies = book[0]
    if available_copies < 1:
        print("No copies available for this book.")
        return

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    if not user:
        print("User not found.")
        return

    issue_date = datetime.now().strftime('%Y-%m-%d')
    query = "INSERT INTO issued (book_id, user_id, issue_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_id, user_id, issue_date))
    cursor.execute("UPDATE books SET copies = copies - 1 WHERE book_id = %s", (book_id,))
    connection.commit()
    print(f"Book ID {book_id} issued to User ID {user_id} on {issue_date}.")

# Function to return a book
def return_book():
    book_id = input("Enter Book ID to return: ")
    user_id = input("Enter User ID: ")

    query = "SELECT issue_id FROM issued WHERE book_id = %s AND user_id = %s AND return_date IS NULL"
    cursor.execute(query, (book_id, user_id))
    record = cursor.fetchone()
    if not record:
        print("No record of this book being issued to this user.")
        return

    return_date = datetime.now().strftime('%Y-%m-%d')
    update_query = "UPDATE issued SET return_date = %s WHERE issue_id = %s"
    cursor.execute(update_query, (return_date, record[0]))
    cursor.execute("UPDATE books SET copies = copies + 1 WHERE book_id = %s", (book_id,))
    connection.commit()
    print(f"Book ID {book_id} returned by User ID {user_id} on {return_date}.")

# Function to add a note for a user
def add_note():
    user_id = input("Enter your User ID: ")
    content = input("Enter note content: ")
    note_date = datetime.now().strftime('%Y-%m-%d')
    query = "INSERT INTO notes (user_id, content, note_date) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, content, note_date))
    connection.commit()
    print("Note added successfully with ID", cursor.lastrowid)

# Function to display notes for a user
def display_notes(user_id):
    print(f"Notes for User ID {user_id}:")
    cursor.execute("SELECT note_id, content, note_date FROM notes WHERE user_id = %s", (user_id,))
    notes = cursor.fetchall()
    if notes:
        for note in notes:
            print("ID:", note[0], "Date:", note[2], "Content:", note[1])
    else:
        print("No notes found for this user.")

# Function to update a note
def update_note():
    note_id = input("Enter Note ID to update: ")
    cursor.execute("SELECT content FROM notes WHERE note_id = %s", (note_id,))
    record = cursor.fetchone()
    if not record:
        print("Note ID not found.")
        return
    print("Current content:", record[0])
    new_content = input("Enter new content: ")
    update_query = "UPDATE notes SET content = %s WHERE note_id = %s"
    cursor.execute(update_query, (new_content, note_id))
    connection.commit()
    print("Note updated successfully.")

# Function to delete a note
def delete_note():
    note_id = input("Enter Note ID to delete: ")
    confirm = input(f"Are you sure you want to delete note {note_id}? (y/n): ")
    if confirm.lower() == 'y':
        cursor.execute("DELETE FROM notes WHERE note_id = %s", (note_id,))
        connection.commit()
        print("Note deleted successfully.")
    else:
        print("Deletion cancelled.")

# Function to search notes for a user
def search_notes():
    user_id = input("Enter your User ID: ")
    keyword = input("Enter keyword to search in notes: ")
    query = "SELECT note_id, content FROM notes WHERE user_id = %s AND content LIKE %s"
    cursor.execute(query, (user_id, '%' + keyword + '%'))
    results = cursor.fetchall()
    if results:
        for note in results:
            print("ID:", note[0], "Content:", note[1])
    else:
        print("No notes found matching that keyword.")

# Main menu for admin users
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add User\n2. Delete User\n3. Update User\n4. Search User\n5. Display All Users")
        print("6. Add Book\n7. Delete Book\n8. Update Book\n9. Search Book\n10. Display All Books")
        print("11. Issue Book\n12. Return Book\n13. Logout")
        choice = input("Enter your choice: ")
        if choice == '1': add_user()
        elif choice == '2': delete_user()
        elif choice == '3': update_user()
        elif choice == '4': search_user()
        elif choice == '5': display_users()
        elif choice == '6': add_book()
        elif choice == '7': delete_book()
        elif choice == '8': update_book()
        elif choice == '9': search_book()
        elif choice == '10': display_books()
        elif choice == '11': issue_book()
        elif choice == '12': return_book()
        elif choice == '13':
            print("Logging out of admin panel.")
            break
        else: print("Invalid option. Please try again.")

# Main menu for normal users
def user_menu(user_id):
    while True:
        print("\n--- User Menu ---")
        print("1. Search Book\n2. Display All Books\n3. Issue Book\n4. Return Book\n5. My Issued Books")
        print("6. Add Note\n7. Delete Note\n8. Update Note\n9. Display My Notes\n10. Search Notes\n11. Logout")
        choice = input("Enter your choice: ")
        if choice == '1': search_book()
        elif choice == '2': display_books()
        elif choice == '3': issue_book()
        elif choice == '4': return_book()
        elif choice == '5':
            cursor.execute("SELECT t1.book_id, t2.title, t1.issue_date, t1.return_date FROM issued t1, books t2 WHERE t1.book_id=t2.book_id and user_id = %s", (user_id,) )
            books = cursor.fetchall()
            if books:
                for b in books: print("Book ID:", b[0], "Title:", b[1],"Issued on:", b[2], "Returned on:", b[3])
            else: print("You have no issued books.")
        elif choice == '6': add_note()
        elif choice == '7': delete_note()
        elif choice == '8': update_note()
        elif choice == '9': display_notes(user_id)
        elif choice == '10': search_notes()
        elif choice == '11':
            print("Logging out of user panel.")
            break
        else: print("Invalid option. Please try again.")

# Main program loop
def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Admin Login\n2. User Login\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            if admin_login(): admin_menu()
        elif choice == '2':
            user = user_login()
            if user: user_menu(user[0])
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else: print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    try:
        main()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")
