BEGIN TRANSACTION;

INSERT INTO orders (customer_id)
VALUES (10);

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (last_insert_rowid(), 1, 1, 79999);

UPDATE products
SET stock = stock - 1
WHERE product_id = 1;

ROLLBACK;







