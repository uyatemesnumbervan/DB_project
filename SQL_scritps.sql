SELECT *
FROM customers
SELECT *
FROM order_items
SELECT *
FROM orders
SELECT *
FROM payments
SELECT *
FROM products

-- 5 ЗАДАЧА
-- SELECT COUNT(status), status
-- FROM orders
-- GROUP BY status
-- 
-- 6 ЗАДАЧА
-- SELECT city, SUM(quantity * price)
-- FROM customers 
-- LEFT JOIN orders ON customers.id = orders.customer_id
-- LEFT JOIN order_items ON orders.id = order_items.order_id
-- WHERE orders.status = 'completed'
-- GROUP BY city
-- ORDER BY SUM(quantity * price) DESC
-- LIMIT 10
-- 
-- 7 ЗАДАЧА
-- SELECT product_id, products.name, SUM(quantity) AS total_quantity
-- FROM products
-- LEFT JOIN order_items ON products.id = order_items.product_id
-- LEFT JOIN orders ON orders.id = order_items.order_id
-- WHERE orders.status = 'completed'
-- GROUP BY products.name, product_id
-- ORDER BY total_quantity DESC
-- LIMIT 10

8 ЗАДАЧА
-- ОБЩАЯ СУММА
-- SELECT SUM(quantity * price) AS total_summa
-- FROM order_items
-- LEFT JOIN orders ON order_items.order_id = orders.id
-- WHERE status = 'completed'

-- ОБЩАЯ СУММА
-- SELECT SUM(revenue)
-- FROM
-- 	(
-- 	SELECT customer_id, name, SUM(order_items.quantity * order_items.price) AS revenue
-- 	FROM customers
-- 	LEFT JOIN orders ON customers.id = orders.customer_id
-- 	LEFT JOIN order_items ON  orders.id = order_items.order_id
-- 	WHERE orders.status = 'completed'
-- 	GROUP BY customer_id, name
-- 	ORDER BY revenue DESC
-- 	)

WITH customer_revenue AS 
(
	SELECT customer_id, customers.name, SUM(order_items.quantity * order_items.price) AS revenue
	FROM customers
	LEFT JOIN orders ON customers.id = orders.customer_id
	LEFT JOIN order_items ON orders.id = order_items.order_id
	WHERE orders.status = 'completed'
	GROUP BY customer_id, name
	ORDER BY revenue DESC
)
SELECT name AS customer_name, revenue, 
SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_revenue, 
SUM(revenue) OVER () AS total_revenue
FROM customer_revenue
ORDER BY revenue DESC



-- 9 ЗАДАЧА
-- WITH dau AS
-- (
-- 	SELECT COUNT(names) AS povtorki
-- 	FROM
-- 	(
-- 		WITH first_buy AS
-- 		(
-- 			SELECT DISTINCT customer_id, name, MIN(order_date) AS min_date
-- 			FROM customers
-- 			LEFT JOIN orders ON customers.id = orders.customer_id
-- 			WHERE status = 'completed'
-- 			GROUP BY customer_id, name
-- 			ORDER BY customer_id, order_date 
-- 		),
-- 		all_buys AS
-- 		(
-- 			SELECT customer_id, name, order_date AS all_dates 
-- 			FROM customers
-- 			LEFT JOIN orders ON customers.id = orders.customer_id
-- 			WHERE status = 'completed'
-- 			GROUP BY order_date
-- 			ORDER BY customer_id, order_date
-- 		)
-- 		SELECT DISTINCT first_buy.customer_id, first_buy.name AS names
-- 		FROM first_buy
-- 		LEFT JOIN all_buys ON first_buy.customer_id = all_buys.customer_id
-- 		WHERE STRFTIME('%Y-%m', first_buy.min_date) = '2024-11' AND STRFTIME('%Y-%m', all_buys.all_dates) = '2024-12'
-- 	)
-- ),
-- nur AS
-- (
-- 	SELECT COUNT(*) AS all_counts
-- 	FROM
-- 	(
-- 		SELECT DISTINCT customer_id, name, MIN(order_date) AS min_date
-- 		FROM customers
-- 		LEFT JOIN orders ON customers.id = orders.customer_id
-- 		WHERE status = 'completed'
-- 		GROUP BY customer_id, name
-- 		ORDER BY customer_id, order_date
-- 	)
-- )
-- SELECT dau.povtorki, nur.all_counts, (cast(dau.povtorki as real) / cast(nur.all_counts as real)) * 100.0
-- FROM dau
-- CROSS JOIN nur

WITH first_buy AS
(
    SELECT customer_id, STRFTIME('%Y-%m', MIN(order_date)) AS first_month
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
),
repeat_buy AS
(
    SELECT DISTINCT first_buy.customer_id, first_buy.first_month
    FROM first_buy 
    JOIN orders 
        ON first_buy.customer_id = orders.customer_id
    WHERE orders.status = 'completed' AND STRFTIME('%Y-%m', orders.order_date) = STRFTIME('%Y-%m', DATE(first_buy.first_month || '-01', '+1 month'))
),
retention AS
(
    SELECT first_buy.first_month, COUNT(DISTINCT first_buy.customer_id) AS customers, COUNT(DISTINCT repeat_buy.customer_id) AS repeat_customers
    FROM first_buy 
    LEFT JOIN repeat_buy  ON first_buy.customer_id = repeat_buy.customer_id AND first_buy.first_month = repeat_buy.first_month
    GROUP BY first_buy.first_month
)

SELECT first_month AS month, customers, repeat_customers,
    ROUND(CAST(repeat_customers AS REAL) / customers * 100, 2) AS retention
FROM retention
ORDER BY month


-- 10 ЗАДАЧА
SELECT *
FROM customers
SELECT *
FROM order_items
SELECT *
FROM orders
SELECT *
FROM payments
SELECT *
FROM products


-- SELECT products.id, products.name, order_items.price AS ЦЕНА_ТОВАРА, quantity, (products.price * 0.7) AS СЕБЕСТОИМОСТЬ, SUM(products.price * quantity) AS REVENUE, 
-- (SUM(products.price * quantity) -  (products.price * 0.7)) AS Profit, (SUM(products.price * quantity) -  (products.price * 0.7)) / SUM(products.price * quantity) * 100 AS Profit_Margin
-- FROM order_items
-- LEFT JOIN products ON order_items.product_id = products.id
-- LEFT JOIN orders ON order_items.order_id = orders.id
-- WHERE orders.status = 'completed'
-- GROUP BY products.name, product_id
-- ORDER BY products.id


SELECT product_id, name, category, order_items.price AS цена_шт, cost AS себестоимость_шт, SUM(quantity * order_items.price) AS выручка, SUM(quantity * cost) AS себестоимость,
SUM(quantity * order_items.price) - SUM(quantity * cost) AS прибыль, 
(((SUM(quantity * order_items.price) - SUM(quantity * cost)) / SUM(quantity * order_items.price)) * 100) AS profit 
FROM order_items
LEFT JOIN products ON order_items.product_id = products.id
LEFT JOIN orders ON order_items.order_id = orders.id
WHERE orders.status = 'completed'
GROUP BY product_id, products.name

SELECT product_id, name, category, order_items.price AS цена_шт, cost AS себестоимость_шт, SUM(quantity * order_items.price) AS выручка, SUM(quantity * cost) AS себестоимость,
SUM(quantity * order_items.price) - SUM(quantity * cost) AS прибыль, 
(((SUM(quantity * order_items.price) - SUM(quantity * cost)) / SUM(quantity * order_items.price)) * 100) AS profit 
FROM order_items
LEFT JOIN products ON order_items.product_id = products.id
LEFT JOIN orders ON order_items.order_id = orders.id
WHERE orders.status = 'completed'
GROUP BY product_id, products.name






