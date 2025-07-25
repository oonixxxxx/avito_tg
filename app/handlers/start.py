from aiogram import Router, types
from aiogram.filters import Command
import sqlite3

router = Router(name="start-main-router")

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    
    # Подключаемся к базе данных
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    try:
        # Проверяем наличие пользователя в базе
        c.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        exists = c.fetchone()
        
        if not exists:
            # Добавляем нового пользователя
            c.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            conn.commit()
            await message.answer("✅ Ваш ID успешно добавлен в базу данных!")
        else:
            await message.answer("ℹ️ Ваш ID уже был в базе данных")
    
    except Exception as e:
        print(f"Ошибка при работе с БД: {e}")
        await message.answer("❌ Произошла ошибка при обработке запроса")
    
    finally:
        # Всегда закрываем соединение
        conn.close()

# Обработчик команды /main
@router.message(Command("main"))
async def cmd_main(message: types.Message):
    user_id = message.from_user.id
    
    # Подключаемся к базе данных
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    try:
        # Проверяем наличие пользователя в базе
        c.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        exists = c.fetchone()
        
        if not exists:
            # Добавляем нового пользователя
            c.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            conn.commit()
            await message.answer("✅ Ваш ID успешно добавлен в базу данных!")
        else:
            await message.answer("ℹ️ Ваш ID уже был в базе данных")
    
    except Exception as e:
        print(f"Ошибка при работе с БД: {e}")
        await message.answer("❌ Произошла ошибка при обработке запроса")
    
    finally:
        # Всегда закрываем соединение
        conn.close()