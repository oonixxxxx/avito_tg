from aiogram import types, F
from aiogram.filters import Command
import sqlite3
from aiogram import Router, types
from aiogram.filters import Command
import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаем клавиатуру для навигации
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="/catalog"),
        InlineKeyboardButton(text="/my_products"),
        InlineKeyboardButton(text='/helper')
    ]
])