from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_my_items_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает мои товары клавиатуру с кнопками Каталог и Корзина
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="/На главную")
    kb.button(text='/Добавить товар')
    kb.button(text='/Удалить товар')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)