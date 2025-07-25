from aiogram import Bot, Dispatcher

from src.bot.handlers import start, help, catalog, my_items, miniapp
from src.bot.config import BOT_TOKEN

async def main():
    try:
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        # Регистрация роутеров
        dp.include_routers(
            start.router,
            help.router,
            catalog.router,
            my_items.router,
            miniapp.router
        )

        # Запуск бота
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"Bot failed to start: {e}")
        return 0 
    finally:
        print("Bot stopped")