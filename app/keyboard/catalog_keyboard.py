from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.handlers.functions.all_functions import get_total_products

total_products = get_total_products()
    
if total_products != 0:
    # Создаем клавиатуру для навигации
    new_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⬅️", callback_data="catalog_prev_0"),
        InlineKeyboardButton(text="1/{}".format(total_products), 
            callback_data="current_position"),
        InlineKeyboardButton(text="➡️", callback_data="catalog_next_0")
    ]
    ])