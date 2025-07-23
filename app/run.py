import asyncio
from src.bot.bot_main import main

if __name__ == "__main__":
    try:
        print('Бот запущен')
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Critical error: {e}")