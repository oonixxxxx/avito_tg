import sqlite3

# Создание базы данных и таблиц
def create_db():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    
    # Таблица пользователей
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 user_id INTEGER PRIMARY KEY,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Таблица товаров
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                 product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER NOT NULL,
                 description TEXT NOT NULL,
                 photo_file_id TEXT NOT NULL,
                 added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                 FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    
    conn.commit()
    conn.close()