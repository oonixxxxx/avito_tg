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

def get_product_by_id(product_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT product_id, description, photo_file_id FROM products WHERE product_id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product

def update_published_message(product_id, message_id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("UPDATE products SET published_message_id = ? WHERE product_id = ?", (message_id, product_id))
    conn.commit()
    conn.close()

# Публикация товара в канале
async def publish_to_channel(product_id, description, photo_file_id):
    try:
        message = await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo_file_id,
            caption=f"🆕 Новый товар!\n\n{description}\n\nID: {product_id}"
        )
        update_published_message(product_id, message.message_id)
        return message.message_id
    except Exception as e:
        logger.error(f"Ошибка публикации в канал: {e}")
        return None