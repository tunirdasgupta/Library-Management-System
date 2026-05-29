# Library Management System

## Overview

The idea for the project came from Vivekananda Pathagar, a small neighbourhood library that I have visited since childhood. Over the years, I noticed that activities such as cataloguing books, tracking borrowers, and managing inventory were handled manually. This inspired me to explore how software could be used to make these processes more efficient.

The application allows administrators to manage books and users, while members can search the catalogue, borrow and return books, and maintain personal reading notes

---

## Problem Statement

Many small libraries rely on manual record-keeping systems. While these systems work, they can be time-consuming, difficult to manage, and prone to errors.

The objective of this project was to design a software solution that could automate common library operations and provide a more organized way of managing books, users, and borrowing records.

---

## Features

### Administrator Functions

- Administrator login
- Add, update, delete, and search books
- Add, update, delete, and search users
- View all books and users
- Issue books to members
- Process book returns

### Member Functions

- Member login
- Search books
- View available books
- Borrow books
- Return books
- View borrowing history
- Create, update, delete, and search personal reading notes
---

## Technologies Used

- Python
- MySQL
- SQL
- MySQL Connector/Python
---

## Database Design

The system uses a relational database consisting of the following entities:


| Table | Purpose |
|---------|---------|
| Admin | Stores administrator credentials |
| Users | Stores member information |
| Books | Stores book inventory details |
| Issued | Tracks issued and returned books |
| Notes | Stores personal reading notes |
---


## Security Features

The project incorporates several security and validation measures:

- Parameterized SQL queries to reduce the risk of SQL injection attacks
- Input validation for user data
- Role-based access control for administrators and members
- Authentication-based access to application features
---

# 📂 Project Structure

```text
Library-Management-System/
│
├── Screenshots/
│   ├── Screenshots - Admin Functions.pdf
│   └── Screenshots - User Functions.pdf
│
├── .gitattributes
├── .gitignore
├── LIBRARY.sql
├── Project Overview.pdf
├── README.md
└── library.py
```

---

## 📌 File Descriptions

| File / Folder          | Description                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| `Screenshots/`         | Contains PDF files with screenshots of administrator and user functionalities |
| `library.py`           | Main Python application containing the Library Management System logic        |
| `LIBRARY.sql`          | SQL file containing the database schema and table definitions                 |
| `Project Overview.pdf` | Project documentation and overview                                            |
| `README.md`            | Repository documentation and setup guide                                      |
| `.gitignore`           | Specifies files ignored by Git                                                |
| `.gitattributes`       | Git configuration attributes file                                             |

---

# Setup Instructions

Follow these steps to set up and run the project on your system.

---

## 1. Clone the Repository

Open Terminal / Command Prompt and run:

```bash
git clone https://github.com/tunirdasgupta/Library-Management-System.git
cd Library-Management-System
```

---

## 2. Install Python Dependencies

Install the required MySQL connector package:

```bash
pip install mysql-connector-python
```

---

## 3. Install and Start MySQL

Make sure MySQL Server is installed and running on your system.

You can download MySQL from:

https://dev.mysql.com/downloads/mysql/

---

## 4. Create the Database

Open MySQL Command Line Client or MySQL Workbench and run:

```sql
CREATE DATABASE library_db;
USE library_db;
```

Then execute the SQL schema file:

```sql
SOURCE LIBRARY.sql;
```

Alternatively, you can manually copy and execute the contents of `LIBRARY.sql`.

---

## 5. Configure Database Credentials

Open `library.py` and update the MySQL connection details:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library_db"
)
```

Replace:

* `your_username` with your MySQL username
* `your_password` with your MySQL password

---

## 6. Run the Application

Run the Python program using:

```bash
python library.py
```

---

# Requirements

* Python 3.x
* MySQL Server
* mysql-connector-python package

---

# Notes

* Ensure MySQL Server is running before starting the application.
* The database schema must be imported successfully before running the program.
* This is a console-based application and runs entirely in the terminal.

---

## What I Learned

Through this project, I gained practical experience in:

- Python programming
- Database design using MySQL
- SQL query development
- Software architecture
- User authentication and authorization
- Secure coding practices
---


## Future Improvements

Potential future enhancements include:

- Graphical User Interface (GUI)
- Password encryption
- Format validation (Email, telephone, Year, etc)
- Email notifications
- Book recommendation system
- Analytics dashboard
---

## Acknowledgements

- I received guidance and encouragement from my Computer Science tutor (Mr. Sudipta Naskar, Assistant teacher of Computer Science at St. Augustine's Day School, Kolkata, email: contact.snaskar@gmail.com) during the design and development of the application.
- My computer science tutor helped me publish the project repository on GitHub and prepare associated documents such as Project Overview, Screenshots, Readme etc.
- I used LLMs such as ChatGPT and Google Gemini to help with learning and debugging during development. These AI tools helped me fix errors and implement features such as protected password entry, validation of fields (emails, phone number, year etc). I also referenced ChatGPT to help me draft the Readme.md documentation and plan the GitHub project structure.
---

## Author

**Tunir Dasgupta**

Python | MySQL | Database Design | Software Development