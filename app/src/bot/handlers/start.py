from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.keyboard_start import get_mainkeyboard
from src.bot.db import cursor

router = Router(name="start-router")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()

    # Добавляем нового пользователя в базу данных
    try:
        if not result:
            cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (user_id, username, first_name, last_name))
            conn.commit()
            await message.answer(f"Привет! Ты успешно зарегистрирован.", reply_markup=get_mainkeyboard())
        else:
            await message.answer(f"Ты уже зарегистрирован.", reply_markup=get_mainkeyboard())
    except Exception as e:
        print(f"Ошибка в обработчике start: {e}")
        return 0

@router.message(Command("На главную"))
async def cmd_main(message: types.Message):
    try:
        await message.answer(
            f"Это стартовое сообщение бота.",
            reply_markup=get_mainkeyboard()
        )
    except Exception as e:
        print(f"Ошибка в обработчике start: {e}")
        return 0