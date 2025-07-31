from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

from app.keyboard.catalog_keyboard import new_keyboard, update_keyboard

router = Router(name="catalog-router")

class DataBase:
    # Вспомогательные функции для работы с базой данных
    def get_total_products(self):
        try:
            conn = sqlite3.connect('shop.db')
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM products")
            total = c.fetchone()[0]
            return total if total is not None else 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return 0
        finally:
            conn.close()

    def get_product_by_index(self, index):
        try:
            conn = sqlite3.connect('shop.db')
            c = conn.cursor()
            c.execute("SELECT description, photo_file_id FROM products ORDER BY product_id LIMIT 1 OFFSET ?", (index,))
            product = c.fetchone()
            return product if product else (None, None)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None, None
        finally:
            conn.close()

# Инициализация базы данных
db = DataBase()

# Обработчик команды /catalog
@router.message(Command("catalog"))
async def cmd_catalog(message: types.Message):
    total_products = db.get_total_products()
    
    if total_products == 0:
        await message.answer("📭 Каталог товаров пуст")
        return
        
    # Получаем первый товар
    description, photo_file_id = db.get_product_by_index(0)
    if not photo_file_id:
        await message.answer("⚠️ Не удалось загрузить товар")
        return

    await message.answer_photo(
        photo=photo_file_id,
        caption=f"Описание: {description}",
        reply_markup=new_keyboard
    )

# Обработчик инлайн-кнопок каталога
@router.callback_query(F.data.startswith("catalog_"))
async def catalog_callback_handler(callback: types.CallbackQuery):
    data = callback.data
    total_products = db.get_total_products()
    
    if total_products == 0:
        await callback.answer("Каталог пуст!", show_alert=True)
        return
    
    # Извлекаем действие и текущий индекс
    try:
        action, current_index_str = data.split("_")[1:]
        current_index = int(current_index_str)
    except (ValueError, IndexError):
        await callback.answer("Ошибка обработки запроса", show_alert=True)
        return
    
    # Обработка навигации
    if action == "prev":
        new_index = current_index - 1 if current_index > 0 else total_products - 1
    elif action == "next":
        new_index = current_index + 1 if current_index < total_products - 1 else 0
    else:
        await callback.answer("Неизвестное действие", show_alert=True)
        return
    
    # Получаем товар по новому индексу
    description, photo_file_id = db.get_product_by_index(new_index)
    if not photo_file_id:
        await callback.answer("Ошибка загрузки товара", show_alert=True)
        return
    
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
    try:
        media = types.InputMediaPhoto(media=photo_file_id, 
                                   caption=f"Описание: {description}")
        await callback.message.edit_media(media, reply_markup=keyboard)
        await callback.answer()
    except Exception as e:
        print(f"Error editing message: {e}")
        await callback.answer("Произошла ошибка при обновлении", show_alert=True)