# SQLite database operations for a simple inventory system
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    try:
        yield conn
    finally:
        conn.close()

class InventoryDB:
    def __init__(self):
        self.init_db()
    
    def init_db(self):
        with get_db_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    category TEXT
                )
            ''')
    
    def add_product(self, name, price, quantity, category):
        with get_db_connection() as conn:
            conn.execute(
                'INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)',
                (name, price, quantity, category)
            )
            conn.commit()
    
    def get_products(self, category=None):
        with get_db_connection() as conn:
            if category:
                result = conn.execute(
                    'SELECT * FROM products WHERE category = ?', (category,)
                )
            else:
                result = conn.execute('SELECT * FROM products')
            return result.fetchall()
    
    def update_quantity(self, product_id, new_quantity):
        with get_db_connection() as conn:
            conn.execute(
                'UPDATE products SET quantity = ? WHERE id = ?',
                (new_quantity, product_id)
            )
            conn.commit()

# Usage
db = InventoryDB()
db.add_product('Laptop', 999.99, 10, 'Electronics')
db.add_product('Book', 19.99, 50, 'Education')
print("All products:", db.get_products())
print("Electronics:", db.get_products('Electronics'))
