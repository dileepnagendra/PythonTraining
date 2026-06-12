-- SELECT

-- SELECT* from customers;
-- SELECT name,city FROM customers;
-- SELECT name AS cutsomer_name,city FROM customers;

-- WHERE

-- SELECT* from customers WHERE city = 'Bangalore';

-- SELECT* from products WHERE price<2000 AND stock<200;

-- SELECT* from customers 
-- WHERE city = 'Bangalore' or city = 'Mumbai';

-- SELECT* from customers 
-- WHERE city IN ('Bangalore','Mumbai','Hyderabad');

-- ORDER BY

-- SELECT* FROM products ORDER BY price;
-- SELECT* FROM products ORDER BY price DESC;

-- SELECT product_name,price FROM products ORDER BY price DESC;

-- SELECT product_name,price FROM products 
-- ORDER BY price DESC LIMIT 3;

-- Aggregations 

-- SELECT SUM(quantity*unit_price) as total_revenue
-- FROM order_items;


-- SELECT SUM(price*stock) as total_worth FROM products;

-- SELECT AVG(quantity*unit_price) as avg_order_value
-- FROM order_items;

-- -- ROUND(value,2)

-- SELECT ROUND(AVG(quantity*unit_price),2) as avg_order_value
-- FROM order_items;


--  GROUP BY
-- SELECT city,COUNT(*) AS total_customers FROM customers 
-- GROUP BY city;

-- SELECT COUNT(*) AS total_customers FROM customers;


-- SELECT COUNT(city) AS total_customers FROM customers;


-- SELECT SUM(price*stock) 
-- AS total_worth_by_category FROM products 
-- GROUP BY category_id;



-- SELECT category_id,SUM(price*stock) 
-- AS total_worth_by_category FROM products 
-- GROUP BY category_id;


-- SELECT  customer_id,COUNT(*) as ordercount from orders
-- GROUP BY customer_id
-- HAVING ordercount >1;







