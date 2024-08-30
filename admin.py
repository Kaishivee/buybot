import sqlite3
from texts import *

connection = sqlite3.connect('database.db ')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)""")


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_product(title, description, price):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (title, description, price))


# add_product(f'{product1}', f'{product1_info}', f'{price1}')
# add_product(f'{product2}', f'{product2_info}', f'{price2}')
# add_product(f'{product3}', f'{product3_info}', f'{price3}')
# add_product(f'{product4}', f'{product4_info}', f'{price4}')

connection.commit()
connection.close()
