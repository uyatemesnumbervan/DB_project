import sqlite3, random
from faker import Faker
from pathlib import Path
fake = Faker()

DB_DIR = Path(__file__).resolve().parent / "MY_DB"
DB_DIR.mkdir(exist_ok=True)

db = sqlite3.connect(DB_DIR / "MY_DB.db")
cur = db.cursor()

cur.executescript("""
PRAGMA journal_mode = WAL;

CREATE TABLE customers(
    id INTEGER PRIMARY KEY,
    name TEXT, email TEXT, city TEXT, created_at TEXT
);

CREATE TABLE products(
    id INTEGER PRIMARY KEY,
    name TEXT, category TEXT, price REAL
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER, order_date TEXT, status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items(
    id INTEGER PRIMARY KEY,
    order_id INTEGER, product_id INTEGER, quantity INTEGER, price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);

CREATE TABLE payments(
    id INTEGER PRIMARY KEY,
    order_id INTEGER, method TEXT, amount REAL, status TEXT,
    FOREIGN KEY(order_id) REFERENCES orders(id)
);
""")

# Customers
customers = [
    (i, fake.name(), fake.email(), fake.city(), fake.date_time_between("-3y", "now"))
    for i in range(1, 50_001)
]
cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?)", customers)

# Products
categories = ["Electronics", "Clothing", "Home", "Sports", "Beauty", "Books", "Gaming"]
products = [
    (i, fake.catch_phrase(), random.choice(categories), round(random.uniform(5, 3000), 2))
    for i in range(1, 5_001)
]
cur.executemany("INSERT INTO products VALUES (?,?,?,?)", products)

# Orders + items + payments
statuses = ["completed", "completed", "completed", "cancelled", "returned"]
methods = ["card", "cash", "paypal", "bank_transfer"]

for start in range(1, 500_001, 10_000):
    orders, items, payments = [], [], []

    for oid in range(start, min(start + 10_000, 500_001)):
        customer = random.randint(1, 50_000)
        date = fake.date_time_between("-2y", "now")
        status = random.choice(statuses)

        orders.append((oid, customer, date, status))

        total = 0
        for _ in range(random.randint(1, 6)):
            pid = random.randint(1, 5_000)
            qty = random.randint(1, 5)
            price = products[pid - 1][3]
            # print(pid)
            total += qty * price
            items.append((None, oid, pid, qty, price))

        payments.append((
            None, oid, random.choice(methods),
            round(total, 2),
            "paid" if status == "completed" else "failed"
        ))

    cur.executemany("INSERT INTO orders VALUES (?,?,?,?)", orders)
    cur.executemany("INSERT INTO order_items VALUES (?,?,?,?,?)", items)
    cur.executemany("INSERT INTO payments VALUES (?,?,?,?,?)", payments)
    db.commit()

db.close()
print("Done!")
