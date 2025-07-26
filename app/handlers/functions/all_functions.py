import sqlite3

# Вспомогательные функции для работы с БД
def get_total_products():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    total = c.fetchone()[0]
    conn.close()
    return total

def get_product_by_index(index):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT description, photo_file_id FROM products ORDER BY product_id LIMIT 1 OFFSET ?", (index,))
    product = c.fetchone()
    conn.close()
    return product

#Функция поиска товара
def search_products(query):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    
    # Используем полнотекстовый поиск, если доступен
    try:
        c.execute("SELECT product_id, description, photo_file_id FROM products WHERE description LIKE ?", 
                 (f'%{query}%',))
    except:
        # Простой поиск если FTS не поддерживается
        c.execute("SELECT product_id, description, photo_file_id FROM products WHERE description LIKE ?", 
                 (f'%{query}%',))
    
    results = c.fetchall()
    conn.close()
    return results

#получаем продукт по id
def get_product_by_id(product_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT product_id, description, photo_file_id FROM products WHERE product_id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product

#обновляем
def update_published_message(product_id, message_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("UPDATE products SET published_message_id = ? WHERE product_id = ?", (message_id, product_id))
    conn.commit()
    conn.close()