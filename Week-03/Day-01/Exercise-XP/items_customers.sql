-- CREATE TABLE items (
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR(100) NOT NULL,
-- item_price DECIMAL(10, 2) NOT NULL
-- );

-- SELECT * FROM items

-- CREATE TABLE customers (
-- customer_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50)
-- );

-- SELECT * FROM customers

-- INSERT INTO customers (first_name, last_name)
-- VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')

-- SELECT * FROM items WHERE item_price > 80;
-- SELECT * FROM items WHERE item_price <= 300;

-- SELECT * FROM customers WHERE last_name = 'Smith'; -- Outcome: no results returned since no such customer
-- SELECT * FROM customers WHERE last_name = 'Jones';
-- SELECT * FROM customers WHERE first_name != 'Scott'