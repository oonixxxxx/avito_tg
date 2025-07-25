import sqlite3

conn = sqlite3.connect('user.bd') #Создание подключения к БД
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    );
''')

conn.commit() #Сохраняем изменения