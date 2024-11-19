-- Exercise _1 DVD Rental: Customer Review

-- SELECT * FROM language
--#Check language of the film
-- SELECT film.title, film.description, language.name FROM film INNER JOIN language ON film.language_id = language.language_id

--#Check language of the film, returns NULL if language has no assigned film
-- SELECT film.title, film.description, language.name FROM film RIGHT JOIN language ON language.language_id = film.language_id

-- CREATE TABLE new_film (
-- nf_id SERIAL PRIMARY KEY,
-- nf_title VARCHAR (100) NOT NULL
-- )

-- INSERT INTO new_film (nf_title) VALUES
-- ('King Pong'),
-- ('Pump Fiction'),
-- ('Whiny-the-Pool'),
-- ('Transmorphers: Revenge on the Poland'),
-- ('Godzmiller'),
-- ('Interfella'),
-- ('Snowbright and the Seven Dawgs');

-- SELECT * FROM new_film

-- CREATE TABLE customer_review (
-- review_id SERIAL PRIMARY KEY,
-- film_id INTEGER REFERENCES new_film(nf_id) ON DELETE CASCADE,
-- language_id INTEGER REFERENCES language(language_id),
-- title VARCHAR (180) NOT NULL,
-- score INTEGER CHECK (score BETWEEN 1 AND 10),
-- review_text TEXT,
-- last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- SELECT * FROM customer_review

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text) 
-- VALUES (
-- (SELECT nf_id FROM new_film WHERE nf_title = 'Snowbright and the Seven Dawgs'),
-- (SELECT language_id FROM language WHERE name = 'German'),
-- 'I wish I knew German',
-- 8,
-- 'Wonderful masterpiece from the studio that brought us SwingingFella, Shreek, Avajar and Tatamic! It would have made more sense story-wise if I knew any German.'),
-- ((SELECT nf_id FROM new_film WHERE nf_title = 'Pump Fiction'),
-- (SELECT language_id FROM language WHERE name = 'English'),
-- 'A must-see guide into the world of plumbing and pools!',
-- 10,
-- 'I wish I could bang myself against the wall with my head to get amnesia and rewatch this movie over and over again! As long as the wall keeps standing and head endures banging.');

-- DELETE FROM new_film WHERE nf_title = 'Snowbright and the Seven Dawgs'
-- SELECT * FROM customer_review
-- SELECT * FROM new_film

-- Exercise _2 DVD Rental: UPDATE and SEARCH queries

-- SELECT * FROM language
--#Adding more languages to more films
-- UPDATE film SET language_id = 3 WHERE film_id IN (8, 16, 32, 64, 128, 256, 512, 768);
-- UPDATE film SET language_id = 2 WHERE film_id IN (10, 20, 40, 80, 160, 320, 640, 980);
-- UPDATE film SET language_id = 4 WHERE film_id IN (15, 25, 45, 85, 165, 325, 645, 985);

-- DROP TABLE customer_review RESTRICT

--#Check how many films have not been returned yet
-- SELECT COUNT(*) AS nonreturned FROM rental WHERE return_date IS NULL

--#Find 30 most expensive movies in nonreturned section
-- SELECT film.title, film.rental_rate, rental.rental_date FROM rental JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- JOIN film ON inventory.film_id = film.film_id WHERE rental.return_date IS NULL ORDER BY film.rental_rate DESC LIMIT 30

--#Friends asking for a movie given keyword 'sumo' and actor name
-- SELECT film.title FROM film 
-- JOIN film_actor ON film.film_id = film_actor.film_id 
-- JOIN actor ON film_actor.actor_id = actor.actor_id 
-- WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' 
-- AND film.description ILIKE '%sumo%';

--#Friend asking for a movie Documentary rated R less than 60 minutes
-- SELECT film.title, category.name FROM film 
-- JOIN film_category ON film.film_id = film_category.film_id 
-- JOIN category ON film_category.category_id = category.category_id 
-- WHERE category.name = 'Documentary' AND film.length < 60 AND film.rating = 'R';

--#Friend asking for a movie rented previously by his friend given rental rate and approximate return date
-- SELECT film.title FROM film 
-- JOIN inventory ON film.film_id = inventory.film_id 
-- JOIN rental ON inventory.inventory_id = rental.inventory_id 
-- JOIN customer ON rental.customer_id = customer.customer_id 
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' 
-- AND rental_rate >4.00 
-- AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

--#Film was watched by given name, has word 'boat' in title or description, very expensive to replace
-- SELECT film.title FROM film
-- JOIN inventory ON film.film_id = inventory.film_id 
-- JOIN rental ON inventory.inventory_id = rental.inventory_id 
-- JOIN customer ON rental.customer_id = customer.customer_id 
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan'
-- AND film.description ILIKE '%boat%' OR film.title ILIKE '%boat%'
-- AND film.replacement_cost = (SELECT MAX(film.replacement_cost) FROM film);