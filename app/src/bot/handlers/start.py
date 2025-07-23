from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.keyboard_start import get_mainkeyboard

router = Router(name="start-router")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        await message.answer(
            f"Это стартовое сообщение бота.",
            reply_markup=get_mainkeyboard()
        )
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