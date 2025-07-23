from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_mainkeyboard() -> ReplyKeyboardMarkup:
    """
    Создает основную клавиатуру с кнопками Каталог и Корзина
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Каталог")
    kb.button(text="Корзина")
    kb.button(text='/Помощь')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)