-- show products which r expensive than avg price of products

-- SELECT product_name,price FROM products
-- WHERE price > (SELECT AVG(price) FROM products);

-- Customers who ordered at least once.
--
-- SELECT name FROM customers
-- WHERE customer_id
--     IN (SELECT DISTINCT customer_id FROM orders);

-- Customers who not ordered at least once.

SELECT name FROM customers
WHERE customer_id 
    NOT IN (SELECT DISTINCT customer_id FROM orders);