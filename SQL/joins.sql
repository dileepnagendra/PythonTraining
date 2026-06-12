-- SELECT DISTINCT name
-- FROM customers
-- JOIN orders ON customers.customer_id == orders.customer_id

-- SELECT name
-- FROM customers
-- INNER JOIN orders ON customers.customer_id == orders.customer_id


-- SELECT DISTINCT name,order_id
-- FROM customers
-- LEFT JOIN orders ON customers.customer_id == orders.customer_id

-- SELECT name, order_id
-- FROM customers
-- JOIN orders ON customers.customer_id == orders.customer_id

-- SELECT name, order_id
-- FROM customers
-- LEFT JOIN orders ON customers.customer_id == orders.customer_id


-- SELECT name, order_id
-- FROM customers c
-- JOIN orders o ON c.customer_id == o.customer_id

-- Customers ordered more than once

-- SELECT name,COUNT(order_id) as order_count
-- FROM customers c
-- JOIN orders o ON c.customer_id == o.customer_id
-- GROUP BY name
-- HAVING order_count>1;

-- What products are ordered so far and their count

-- SELECT product_name, COUNT(order_id)
-- FROM order_items o
-- JOIN products p ON o.product_id == p.product_id
-- GROUP BY product_name;

-- SELECT product_id, COUNT(order_id)
-- FROM order_items
-- GROUP BY product_id;

-- Show what customer names with poducts ordered by each

-- SELECT name,product_name
-- FROM customers c
-- JOIN orders o ON c.customer_id = o.customer_id
-- JOIN order_items oi ON oi.order_id == o.order_id
-- JOIN products p ON oi.product_id == p.product_id