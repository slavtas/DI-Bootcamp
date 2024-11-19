-- #Part I

-- CREATE TABLE Customer (
-- id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE CustomerProfile (
-- id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT false,
-- customer_id INTEGER UNIQUE REFERENCES Customer(id)
-- );

-- INSERT INTO Customer (first_name, last_name) 
-- VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- INSERT INTO CustomerProfile (isLoggedIn, customer_id)
-- VALUES
-- (true, (SELECT id FROM Customer WHERE first_name = 'John')),
-- (false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));

-- SELECT * FROM customerprofile

--#Query1: First name of logged-in customers

-- SELECT customer.first_name FROM Customer 
-- JOIN CustomerProfile ON customer.id = customerprofile.customer_id
-- WHERE customerprofile.isLoggedIn = true;

--#Query2: Show all firs names and logged-in status

-- SELECT customer.first_name, COALESCE(customerprofile.isLoggedIn, false) AS isLoggedIn
-- FROM Customer LEFT JOIN CustomerProfile ON customer.id = customerprofile.customer_id;

--#Query3: Count non-logged-in customers

-- SELECT COUNT(*) AS not_logged_in_count
-- FROM Customer LEFT JOIN CustomerProfile ON customer.id = customerprofile.customer_id
-- WHERE COALESCE(customerprofile.isLoggedIn, false) = false;

--#Part II

-- CREATE TABLE Book (
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR(100) NOT NULL,
-- author VARCHAR(100) NOT NULL
-- );

-- INSERT INTO Book (title, author)
-- VALUES 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee');

-- CREATE TABLE Student (
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR(50) NOT NULL UNIQUE,
-- age INTEGER CHECK (age <= 15)
-- );

-- INSERT INTO Student (name, age)
-- VALUES 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- CREATE TABLE Library (
-- book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- borrowed_date DATE,
-- PRIMARY KEY (book_fk_id, student_fk_id)
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES 
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
-- (SELECT student_id FROM Student WHERE name = 'John'),
-- '2022-02-15'),
-- ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), 
-- (SELECT student_id FROM Student WHERE name = 'Bob'),
-- '2021-03-03'),
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), 
-- (SELECT student_id FROM Student WHERE name = 'Lera'),
-- '2021-05-23'),
-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), 
-- (SELECT student_id FROM Student WHERE name = 'Bob'),
-- '2021-08-12');

--#Query1: Select all columns from the junction table

-- SELECT * FROM Library

--#Query2: Select name of the student and title of the borrowed book

-- SELECT student.name, book.title FROM Library
-- JOIN Book ON library.book_fk_id = book.book_id 
-- JOIN Student ON library.student_fk_id = student.student_id;

--#Query3: Average age of students who borrowed AiW

-- SELECT AVG(student.age) FROM Library 
-- JOIN Book ON library.book_fk_id = book.book_id 
-- JOIN Student ON library.student_fk_id = student.student_id
-- WHERE book.title = 'Alice In Wonderland';

--#Query4: Delete student from Student table, see what happens

-- DELETE FROM Student WHERE name = 'John';

-- SELECT * FROM Library