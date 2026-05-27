-- Create database
CREATE DATABASE library_db;
USE library_db;

-- Admin table (stores admin login credentials)
CREATE TABLE admin (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL);

-- Users (Members) table
CREATE TABLE users (
user_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100),
phone VARCHAR(20),
password VARCHAR(50) NOT NULL
);

-- Books table
CREATE TABLE books (
book_id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
author VARCHAR(255),
publisher VARCHAR(255),
year YEAR,
copies INT DEFAULT 1
);

-- Issued (Borrowing) table
CREATE TABLE issued (
issue_id INT AUTO_INCREMENT PRIMARY KEY,
book_id INT, user_id INT, issue_date DATE,
return_date DATE, FOREIGN KEY (book_id)
REFERENCES books(book_id), FOREIGN KEY (user_id)
REFERENCES users(user_id)
);

-- Notes table (personal notes per user)
CREATE TABLE notes (
note_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
content TEXT,
note_date DATE,
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sample Inserts (optional initial data)
INSERT INTO admin (username, password) VALUES ('admin','admin123');


INSERT INTO users (name, email, phone, password) VALUES ('Alice',
'alice@example.com',
'1234567890',
'alicepw');

INSERT INTO books (title, author, publisher, year, copies) VALUES
('The Great Gatsby',
'F. Scott Fitzgerald',
'Scribner',1984,
3);

INSERT INTO books (title, author, publisher, year, copies) VALUES
('1984',
'George Orwell',
'Secker & Warburg', 1949,
2);

-- Sample query examples:
SELECT * FROM books;
SELECT * FROM users WHERE name LIKE '%Ali%';
INSERT INTO issued (book_id, user_id, issue_date) VALUES (1, 1, CURDATE());
UPDATE issued SET return_date = CURDATE() WHERE issue_id = 1;
INSERT INTO
notes (user_id, content, note_date) VALUES (1,
'Read chapters 1-3'
,
CURDATE());

/*
The above schema defines the tables and shows how to insert and query data. For instance, a Books table like this (using AUTO_INCREMENT and PRIMARY KEY) is common in library systems. The issued tablecorresponds to the Borrowing table in standard designs (it links books and users).

All SQL commands should be parameterized in code; the samples above use literal values only as an illustration.
*/
