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