from aiogram import Router, types
from aiogram.filters import Command

from src.bot.keyboard.keyboard_help import get_helpkeyboard
from src.bot.keyboard.keyboard_start import get_mainkeyboard

router = Router(name="help-router")

@router.message(Command("Помощь"))
async def cmd_help(message: types.Message):
    try:
        await message.answer(
            f"Это help сообщение бота.",
            reply_markup=get_helpkeyboard()
        )
    except Exception as e:
        print(f"Ошибка в обработчике help: {e}")
        return 0