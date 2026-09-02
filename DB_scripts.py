import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

db = sqlite3.connect("MY_DB/MY_DB.db")
cur = db.cursor()

# ----------------------------------------------------------------------------------
# 2 - задача
# result_query = cur.execute("""
# SELECT products.category,
#        SUM(order_items.quantity * order_items.price) AS revenue
# FROM order_items
# JOIN products
#     ON order_items.product_id = products.id
# GROUP BY products.category
# ORDER BY revenue DESC
# LIMIT 10
# """)
#
# df = pd.DataFrame(
#     result_query.fetchall(),
#     columns=['category', 'revenue']
# )
#
# print(df)
#
# plt.bar(df['category'], df['revenue'])
# plt.xlabel('category')
# plt.ylabel('revenue')
# plt.title('Revenue by category')
# plt.xticks(rotation=45)
# plt.show()
#
# db.close()

# ----------------------------------------------------------------------------------
# 1 - задача
# result_query = cur.execute("""
# SELECT STRFTIME('%Y-%m', order_date) AS time1, SUM(amount)
# FROM orders
# LEFT JOIN payments ON orders.id = payments.order_id
# WHERE payments.status = 'paid'
# GROUP BY time1
# ORDER BY time1
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['date', 'amount'])
# print(df)
# df.plot(x='date', y='amount', kind='line', color='blue', marker='s')
# plt.xlabel('date')
# plt.ylabel('amount')
# plt.title('1')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 3 - задача
# result_query = cur.execute("""
# SELECT STRFTIME('%Y-%m', order_date), AVG(amount)
# FROM orders
# LEFT JOIN payments ON orders.id = payments.order_id
# WHERE payments.status = 'paid'
# GROUP BY STRFTIME('%Y-%m', order_date)
# ORDER BY STRFTIME('%Y-%m', order_date)
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['date', 'AVG-amount'])
# print(df)
# df.plot(x='date', y='AVG-amount', kind='line', color='blue', marker='s')
# plt.title('3')
# plt.xlabel('date')
# plt.ylabel('AVG-amount')
# plt.grid(True)
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 4 - задача
# result_query = cur.execute("""
# SELECT customers.id, customers.name, COUNT(orders.id), SUM(amount)
# FROM customers
# JOIN orders ON customers.id = orders.customer_id
# JOIN payments ON orders.id = payments.order_id
# WHERE orders.status = 'completed' AND payments.status = 'paid'
# GROUP BY customers.id, customers.name
# ORDER BY SUM(amount)DESC
# LIMIT 20
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['customers_id', 'name', 'COUNT_orders', 'SUM_amount'])
# print(df)
# plt.barh(df['name'], df['SUM_amount'], color='skyblue')
# plt.xlabel('SUM_amount')
# plt.ylabel(' name')
# plt.title('4')
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 5 задача
# result_query = cur.execute("""
# SELECT COUNT(status), status
# FROM orders
# GROUP BY status
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['COUNT', 'status'])
# print(df)
# plt.bar(df['status'], df['COUNT'])
# plt.xlabel('COUNT')
# plt.ylabel('status')
# plt.title('5')
# plt.xticks(rotation=45)
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 6-7 задача
# result_query = cur.execute("""
# SELECT city, SUM(quantity * price)
# FROM customers
# LEFT JOIN orders ON customers.id = orders.customer_id
# LEFT JOIN order_items ON orders.id = order_items.order_id
# WHERE orders.status = 'completed'
# GROUP BY city
# ORDER BY SUM(quantity * price) DESC
# LIMIT 10
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['city', 'SUM(quantity * price)'])
# print(df)
# plt.bar(df['city'], df['SUM(quantity * price)'])
# plt.xlabel('city')
# plt.ylabel('SUM(quantity * price)')
# plt.title('6')
# plt.xticks(rotation=45)
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 6-7 задача
# result_query = cur.execute("""
# SELECT city, SUM(quantity * price)
# FROM customers
# LEFT JOIN orders ON customers.id = orders.customer_id
# LEFT JOIN order_items ON orders.id = order_items.order_id
# WHERE orders.status = 'completed'
# GROUP BY city
# ORDER BY SUM(quantity * price) DESC
# LIMIT 10
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['city', 'SUM(quantity * price)'])
# print(df)
# plt.bar(df['city'], df['SUM(quantity * price)'])
# plt.xlabel('city')
# plt.ylabel('SUM(quantity * price)')
# plt.title('6')
# plt.xticks(rotation=45)
# plt.show()
# db.close()

# ----------------------------------------------------------------------------------
# 8 задача
# from matplotlib.ticker import PercentFormatter
# result_query = cur.execute("""
# WITH customer_revenue AS
# (
# 	SELECT customer_id, customers.name, SUM(order_items.quantity * order_items.price) AS revenue
# 	FROM customers
# 	LEFT JOIN orders ON customers.id = orders.customer_id
# 	LEFT JOIN order_items ON orders.id = order_items.order_id
# 	WHERE orders.status = 'completed'
# 	GROUP BY customer_id, name
# 	ORDER BY revenue DESC
# )
# SELECT name AS customer_name, revenue,
# SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_revenue,
# SUM(revenue) OVER () AS total_revenue
# FROM customer_revenue
# ORDER BY revenue DESC
# """)
# df = pd.DataFrame(result_query.fetchall(), columns=['customer_name', 'revenue', 'cumulative_revenue', 'total_revenue'])
# print(df)
# df["cumulative_percent"] = (df["cumulative_revenue"] / df["total_revenue"]) * 100
#
# fig, ax1 = plt.subplots(figsize=(10, 5))
#
# x = range(1, len(df) + 1)
#
# ax1.bar(x, df["revenue"])
# ax1.set_xlabel("Клиенты (по убыванию выручки)")
# ax1.set_ylabel("Выручка")
# ax1.set_xticks(range(0, len(df) + 1, 5000))
#
# ax2 = ax1.twinx()
# ax2.plot(x, df["cumulative_percent"])
# ax2.set_ylabel("Накопленный процент")
# ax2.set_ylim(0, 105)
# ax2.yaxis.set_major_formatter(PercentFormatter(xmax=100))
# ax2.axhline(80, linestyle="--", alpha=0.7)
#
# plt.title("Диаграмма Парето (Выручка)")
# plt.tight_layout()
# plt.show()

# ----------------------------------------------------------------------------------
# 9 задача
# result_query = cur.execute("""
# WITH first_buy AS
# (
#     SELECT customer_id, STRFTIME('%Y-%m', MIN(order_date)) AS first_month
#     FROM orders
#     WHERE status = 'completed'
#     GROUP BY customer_id
# ),
# repeat_buy AS
# (
#     SELECT DISTINCT first_buy.customer_id, first_buy.first_month
#     FROM first_buy
#     JOIN orders ON first_buy.customer_id = orders.customer_id
#     WHERE orders.status = 'completed' AND STRFTIME('%Y-%m', orders.order_date) = STRFTIME('%Y-%m', DATE(first_buy.first_month || '-01', '+1 month'))
# ),
# retention AS
# (
#     SELECT first_buy.first_month, COUNT(DISTINCT first_buy.customer_id) AS customers, COUNT(DISTINCT repeat_buy.customer_id) AS repeat_customers
#     FROM first_buy
#     LEFT JOIN repeat_buy  ON first_buy.customer_id = repeat_buy.customer_id AND first_buy.first_month = repeat_buy.first_month
#     GROUP BY first_buy.first_month
# )
# SELECT first_month AS month, customers, repeat_customers, ROUND(CAST(repeat_customers AS REAL) / customers * 100, 2) AS retention
# FROM retention
# ORDER BY month
# """)
#
# df = pd.DataFrame(result_query.fetchall(), columns=['month', 'customers', 'repeat_customers', 'retention'])
# print(df)
#
# plt.figure(figsize=(10, 5))
# plt.plot(df['month'], df['retention'], marker='o')
# plt.title('Customer Retention по месяцам')
#
# plt.xlabel('Месяц первой покупки')
# plt.ylabel('Retention, %')
# plt.xticks(rotation=45)
# plt.grid(True)
#
# plt.show()


# ----------------------------------------------------------------------------------
# 10 задача
# result_query = cur.execute("""
# SELECT product_id, name, category, order_items.price AS цена_шт, cost AS себестоимость_шт, SUM(quantity * order_items.price) AS выручка, SUM(quantity * cost) AS себестоимость,
# SUM(quantity * order_items.price) - SUM(quantity * cost) AS прибыль,
# (((SUM(quantity * order_items.price) - SUM(quantity * cost)) / SUM(quantity * order_items.price)) * 100) AS profit
# FROM order_items
# LEFT JOIN products ON order_items.product_id = products.id
# LEFT JOIN orders ON order_items.order_id = orders.id
# WHERE orders.status = 'completed'
# GROUP BY product_id, products.name
# """)
#
# df = pd.DataFrame(result_query.fetchall(), columns=['product_id', 'name', 'category', 'цена_шт', 'себестоимость_шт', 'выручка', 'себестоимость', 'прибыль', 'profit'])
# print(df)
#
# import matplotlib.pyplot as plt
#
# top20 = df.sort_values('прибыль', ascending=False).head(20)
# plt.figure(figsize=(12, 6))
# x = range(len(top20))
# plt.bar([i - 0.2 for i in x], top20['выручка'], width=0.4, label='Revenue')
# plt.bar([i + 0.2 for i in x], top20['прибыль'], width=0.4, label='Profit')
# plt.xticks(x, top20['name'], rotation=45, ha='right')
# plt.ylabel('Сумма')
# plt.title('Revenue vs Profit — Top 10 товаров')
# plt.legend()
# plt.tight_layout()
# plt.show()



