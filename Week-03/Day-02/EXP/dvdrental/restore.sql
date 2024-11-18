-- Exercise_2 W3D2
-- SELECT * FROM customer -- Returns 599 values
-- SELECT first_name ||' '|| last_name AS full_name FROM customer; -- Displays customer's full name in one column
-- SELECT DISTINCT create_date FROM customer -- Shows the date without duplicates
-- SELECT * FROM customer ORDER BY first_name DESC
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC
-- SELECT address, phone FROM address WHERE district = 'Texas'; -- Simply returns addresses and phones of the customers in Texas

-- SELECT customer.first_name||' '||customer.last_name 
-- AS full_name, address.address, address.phone 
-- FROM customer INNER JOIN address ON customer.customer_id = address.address_id 
-- WHERE district = 'Texas'; -- Same as above but with more details such as full name of the customer

-- SELECT * FROM film WHERE film_id = 15 OR film_id = 150
-- SELECT film_ID, title, description, length, rental_rate FROM film WHERE title = 'Ali Forever'
-- SELECT film_ID, title, description, length, rental_rate FROM film WHERE title LIKE 'Al%'
-- SELECT title, rental_rate FROM film LIMIT 10
-- SELECT title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10
-- SELECT title, rental_rate FROM film ORDER BY rental_rate OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

-- SELECT customer.first_name||' '||customer.last_name AS full_name, payment.amount, payment.payment_date 
-- FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id ORDER BY payment.customer_id;

-- SELECT f.film_id, f.title 
-- FROM film f LEFT JOIN inventory i 
-- ON f.film_id = i.film_id WHERE i.film_id IS NULL;

-- SELECT city.city, country.country
-- FROM country INNER JOIN city
-- ON country.country_id = city.country_id;

-- SELECT customer.first_name||' '||customer.last_name AS full_name, payment.amount, payment.payment_date, staff.staff_id 
-- FROM customer JOIN payment ON customer.customer_id = payment.customer_id JOIN staff ON payment.staff_id = staff.staff_id; -- BONUS