-- CREATE TABLE actors (
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR (50) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL)

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5),
-- ('George','Clooney','06/05/1961', 2);
-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Angelina','Jolie','06/04/1975', 1),
-- ('Jennifer', 'Aniston', '02/11/1969', 0),
-- ('Leonardo', 'DiCaprio', '11/11/1974', 1),
-- ('Brad', 'Pitt', '18/12/1963', 4);

-- SELECT COUNT(actor_id) FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('', 'Doofoos', '', 5); -- Returns ERROR: invalid input syntax for type date: ""

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('', '', '31/12/1999', ) -- Returns ERROR: syntax error at or near ")"

-- Therefore ,y understanding is that when trying to add new actor with some blank fields an ERROR pops up indicating invalid data input