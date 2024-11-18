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

-- SELECT AVG(number_oscars) FROM actors
-- SELECT COUNT(first_name) AS total_actors FROM actors
-- ALTER TABLE actors
-- RENAME COLUMN number_oscars TO oscars
-- SELECT *FROM actors WHERE age BETWEEN '01/01/1960' AND '01/01/1970'
-- SELECT * FROM actors WHERE oscars = (SELECT MAX(oscars) FROM actors)

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );
-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));
-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Troy', 
--     'Written by Brad and Jennifer, the film follows 20-year-old Greek janitor Akhilesus',
--     (SELECT actor_id from actors WHERE first_name='Brad' AND last_name='Pitt')),
--     ( 'World War Z', 
--     'American heist film directed by Brad Pitt and written by Zak Snider.', 
--     (SELECT actor_id from actors WHERE first_name='Brad' AND last_name='Pitt'));
-- SELECT * FROM movies
-- SELECT actors.first_name, actors.last_name, movies.movie_title FROM actors INNER JOIN movies ON actors.actor_id = movies.actor_playing_id;

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR (50) NOT NULL,
-- producer_last_name VARCHAR (50) NOT NULL,
-- movie_producer_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_producer_id) REFERENCES movies (movie_id)
-- );
-- INSERT INTO producers (producer_name, producer_last_name, movie_producer_id) 
-- VALUES ( 'Lawrence', 'Bender',(SELECT movie_id FROM movies WHERE movie_title = 'Good Will Hunting'))
-- SELECT * FROM producers

-- SELECT producers.producer_name, producer_last_name, movies.movie_title FROM producers INNER JOIN movies ON producers.movie_producer_id = movies.movie_id

--Left JOIN
-- SELECT actors.first_name, actors.last_name, movies.movie_title FROM actors LEFT OUTER JOIN movies ON actors.actor_id = movies.actor_playing_id
--Right JOIN
-- SELECT actors.first_name, actors.last_name, movies.movie_title 
-- FROM movies LEFT OUTER JOIN actors 
-- ON actors.actor_id = movies.actor_playing_id

-- CREATE TABLE countries (
-- country_id SERIAL PRIMARY KEY,
-- country_name VARCHAR(50) NOT NULL
-- )

-- INSERT INTO countries (country_name) VALUES
-- ('USA'),
-- ('Canada'),
-- ('UK'),
-- ('Australia'),
-- ('Germany');

-- SELECT actors.actor_id, actors.first_name, countries.country_name 
-- FROM actors 
-- INNER JOIN countries ON actors.actor_id = countries.country_id;

-- SELECT actors.actor_id, actors.first_name, countries.country_name 
-- FROM actors LEFT OUTER JOIN countries ON actors.actor_id = countries.country_id;

-- SELECT actors.actor_id, actors.first_name, countries.country_name 
-- FROM actors RIGHT OUTER JOIN countries ON actors.actor_id = countries.country_id;

-- SELECT actors.actor_id, actors.first_name, countries.country_name 
-- FROM actors FULL OUTER JOIN countries ON actors.actor_id = countries.country_id;

-- UPDATE actors
-- SET age = '01//01/1970' WHERE first_name = 'Matt' AND last_name = 'Damon'
-- RETURNING
-- actor_id,
-- first_name,
-- last_name,
-- age;

-- DELETE FROM actors WHERE actor_id = 4
-- RETURNING actor_id, first_name, last_name, oscars;