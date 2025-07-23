from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.keyboard_start import get_mainkeyboard

router = Router(name="my-items-router")

@router.message(Command("Мои товары"))
async def cmd_my_items(message: types.Message):
    try:
        await message.answer(
            f"Это стартовое сообщение бота.",
            reply_markup=get_mainkeyboard()
        )
    except Exception as e:
        print(f"Ошибка в обработчике start: {e}")
        return 0