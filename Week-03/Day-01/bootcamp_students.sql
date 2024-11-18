-- CREATE TABLE students (
-- student_id SERIAL PRIMARY KEY,
-- last_name VARCHAR(50) NOT NULL,
-- first_name VARCHAR(50) NOT NULL,
-- birth_date DATE NOT NULL
-- );

-- INSERT INTO students (last_name, first_name, birth_date)
-- VALUES
-- ('Benichou', 'Marc', '02/11/1988'),
-- ('Cohen', 'Yoan', '03/12/2010'),
-- ('Benichou', 'Lea', '27/07/1987'),
-- ('Dux', 'Amelia', '07/04/1996'),
-- ('Grez', 'David', '14/06/2003'),
-- ('Simpson', 'Homer', '03/10/1980');

-- SELECT * FROM students
-- SELECT first_name, last_name FROM students
-- SELECT first_name, last_name FROM students WHERE student_id = 2
-- SELECT first_name, last_name FROM students WHERE first_name = 'Marc' AND last_name = 'Benichou'
-- SELECT last_name, first_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'
-- SELECT first_name FROM students WHERE first_name LIKE '%a%'
-- SELECT first_name FROM students WHERE first_name LIKE 'A%'
-- SELECT first_name FROM students WHERE first_name LIKE '%a'
-- SELECT first_name FROM students WHERE first_name LIKE '%a_'
-- SELECT student_id, first_name, last_name FROM students WHERE student_id IN (1,3)
SELECT * FROM students WHERE birth_date >= '01/01/2000'