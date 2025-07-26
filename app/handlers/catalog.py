from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

from app.keyboard.catalog_keyboard import new_keyboard, update_keyboard

router = Router(name="catalog-router")

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

# Обработчик команды /catalog
@router.message(Command("catalog"))
async def cmd_catalog(message: types.Message):
    total_products = get_total_products()
    
    if total_products == 0:
        await message.answer("📭 Каталог товаров пуст")
        return
        
    # Создаем клавиатуру для навигации
    keyboard = new_keyboard #из модуля с класиватурами
    
    # Получаем первый товар
    product = get_product_by_index(0)
    if product:
        description, photo_file_id = product
        await message.answer_photo(
            photo=photo_file_id,
            caption=f"Описание: {description}",
            reply_markup=keyboard
        )

# Обработчик инлайн-кнопок каталога
@router.callback_query(F.data.startswith("catalog_"))
async def catalog_callback_handler(callback: types.CallbackQuery):
    data = callback.data
    total_products = get_total_products()
    
    if total_products == 0:
        await callback.answer("Каталог пуст!")
        return
    
    # Извлекаем действие и текущий индекс
    action, current_index_str = data.split("_")[1:]
    current_index = int(current_index_str)
    new_index = current_index
    
    # Обработка навигации
    if action == "prev":
        new_index = (current_index - 1) % total_products
    elif action == "next":
        new_index = (current_index + 1) % total_products
    
    # Получаем товар по новому индексу
    product = get_product_by_index(new_index)
    if not product:
        await callback.answer("Ошибка загрузки товара")
        return
    
    description, photo_file_id = product
    
    # Обновляем клавиатуру
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"catalog_prev_{new_index}"),
            InlineKeyboardButton(text=f"{new_index+1}/{total_products}", 
                                callback_data="current_position"),
            InlineKeyboardButton(text="➡️", callback_data=f"catalog_next_{new_index}")
        ]
    ])
    
    # Редактируем сообщение
    media = types.InputMediaPhoto(media=photo_file_id, 
                                caption=f"Описание: {description}")
    
    await callback.message.edit_media(media, reply_markup=keyboard)
    await callback.answer()