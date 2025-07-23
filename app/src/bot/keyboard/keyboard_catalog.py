from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_catalogkeyboard() -> ReplyKeyboardMarkup:
    """
    Создает catalog клавиатуру с кнопками На главную и Тех поддержка
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="На главную")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)