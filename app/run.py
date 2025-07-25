from aiogram import Bot, Dispatcher
import asyncio

from database import create_db
from config import BOT_TOKEN
from handlers import start, add, catalog, my_products

async def main():
    try:
        # Инициализация бота и диспетчера
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        print('Регестрируем роутеры')

        # Регистрация роутеров
        dp.include_routers(
            start.router,
            add.router,
            catalog.router,
            my_products.router
        )

        print('Создаем базу данных...')
        create_db()  # Создаем таблицу при запуске
        print('База данных создана')
        print('Запускаем бота')
        print('Бот запущен')
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Bot failed to start: {e}")
        raise
    finally:
        print("Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())