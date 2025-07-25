from aiogram import types, F
from aiogram.filters import Command
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router(name="start-router")

# Обработчик команды /my_products
@router.message(Command("my_products"))
async def cmd_my_products(message: types.Message):
    user_id = message.from_user.id
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    
    try:
        c.execute("SELECT description, photo_file_id FROM products WHERE user_id = ?", (user_id,))
        products = c.fetchall()
        
        if not products:
            await message.answer("📭 У вас нет добавленных товаров")
            return
            
        for i, (desc, file_id) in enumerate(products, 1):
            await message.answer_photo(
                photo=file_id,
                caption=f"Товар #{i}\nОписание: {desc}"
            )
            
    except Exception as e:
        print(f"Ошибка при получении товаров: {e}")
        await message.answer("❌ Ошибка при загрузке ваших товаров")
    
    finally:
        conn.close()