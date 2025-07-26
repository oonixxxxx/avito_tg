from aiogram import Router, types
from aiogram.filters import Command
import sqlite3

from app.config import admin_id

router = Router(name="helper-router")

# Обработчик команды /help
@router.message(Command("help"))
async def cmd_start(message: types.Message):
    try:
        await message.answer(f"Если возникли ошибки напишите администратору {admin_id}")    
    except Exception as e:
        print(f"Ошибка при работе роутера /help: {e}")
        await message.answer("❌ Произошла ошибка при обработке запроса")