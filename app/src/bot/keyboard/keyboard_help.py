from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_helpkeyboard() -> ReplyKeyboardMarkup:
    """
    Создает help клавиатуру с кнопками На главную и Тех поддержка
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="На главную")
    kb.button(text="Тех поддержка")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)