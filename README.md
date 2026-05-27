\# Library Management System



\## Overview



This project is a Python and MySQL-based Library Management System developed as part of my Class XII Computer Science project.



The idea for the project came from Vivekananda Pathagar, a small neighbourhood library that I have visited since childhood. Over the years, I noticed that activities such as cataloguing books, tracking borrowers, and managing inventory were handled manually. This inspired me to explore how software could be used to make these processes more efficient.



The application allows administrators to manage books and users, while members can search the catalogue, borrow and return books, and maintain personal reading notes.



\---



\## Problem Statement



Many small libraries rely on manual record-keeping systems. While these systems work, they can be time-consuming, difficult to manage, and prone to errors.



The objective of this project was to design a software solution that could automate common library operations and provide a more organized way of managing books, users, and borrowing records.



\---



\## Features



\### Administrator Functions



\- Administrator login

\- Add, update, delete, and search books

\- Add, update, delete, and search users

\- View all books and users

\- Issue books to members

\- Process book returns



\### Member Functions



\- Member login

\- Search books

\- View available books

\- Borrow books

\- Return books

\- View borrowing history

\- Create, update, delete, and search personal reading notes



\---



\## Technologies Used



\- Python

\- MySQL

\- SQL

\- MySQL Connector/Python



\---



\## Database Design



The system uses a relational database consisting of the following entities:



| Table | Purpose |

|---------|---------|

| Admin | Stores administrator credentials |

| Users | Stores member information |

| Books | Stores book inventory details |

| Issued | Tracks issued and returned books |

| Notes | Stores personal reading notes |



\---



\## Security Features



The project incorporates several security and validation measures:



\- Parameterized SQL queries to reduce the risk of SQL injection attacks

\- Input validation for user data

\- Role-based access control for administrators and members

\- Authentication-based access to application features



\---



\## What I Learned



Through this project, I gained practical experience in:



\- Python programming

\- Database design using MySQL

\- SQL query development

\- Software architecture

\- User authentication and authorization

\- Secure coding practices



More importantly, the project helped me understand that technology is not only about writing code but also about understanding people, workflows, and information management.



\---



\## Future Improvements



Potential future enhancements include:



\- Graphical User Interface (GUI)

\- Barcode-based book management

\- Email notifications

\- Book recommendation system

\- Analytics dashboard

\- Cloud deployment



\---



\## Repository Contents



```text

Library-Management-System/

│

├── README.md

├── library\_management.py

├── database\_schema.sql

├── Library\_Management\_System\_Project\_Summary.pdf

├── CBSE\_Project\_Report.pdf

└── screenshots/

```



\---



\## Screenshots



Screenshots of the application are available in the `screenshots` folder.



\---



\## Author



\*\*Tunir Dasgupta\*\*



Python | MySQL | Database Design | Software Development

