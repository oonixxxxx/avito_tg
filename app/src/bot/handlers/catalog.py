from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.keyboard_catalog import get_catalogkeyboard

router = Router(name="catalog-router")

@router.message(Command("Каталог"))
async def cmd_catalog(message: types.Message):
    try:
        await message.answer(
            f"Это catalog сообщение бота.",
            reply_markup=get_catalogkeyboard()
        )
    except Exception as e:
        print(f"Ошибка в обработчике help: {e}")
        return 0