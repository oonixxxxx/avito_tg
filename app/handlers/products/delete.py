import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import asyncio
import re

# Удаление товара
@dp.callback_query(F.data.startswith("delete_"))
async def delete_product_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    product_id = int(callback.data.split("_")[1])
    
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    
    try:
        # Проверяем владельца товара
        c.execute("SELECT user_id, published_message_id FROM products WHERE product_id = ?", (product_id,))
        product = c.fetchone()
        
        if not product:
            await callback.answer("Товар не найден")
            return
            
        owner_id, message_id = product
        
        # Проверяем права на удаление
        if user_id != owner_id and user_id != ADMIN_ID:
            await callback.answer("❌ У вас нет прав для удаления этого товара")
            return
            
        # Удаляем товар из БД
        c.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        conn.commit()
        
        # Пытаемся удалить сообщение из канала
        if message_id:
            try:
                await bot.delete_message(chat_id=CHANNEL_ID, message_id=message_id)
            except Exception as e:
                logger.error(f"Ошибка удаления сообщения из канала: {e}")
        
        await callback.answer("✅ Товар удален")
        await callback.message.edit_caption(caption=f"❌ Товар удален\nID: {product_id}")
        
    except Exception as e:
        logger.error(f"Ошибка удаления товара: {e}")
        await callback.answer("❌ Ошибка при удалении товара")
    
    finally:
        conn.close()

# Команда для администратора - синхронизация канала
@dp.message(Command("sync_channel"))
async def cmd_sync_channel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Эта команда только для администратора")
        return
        
    await message.answer("🔄 Начинаю синхронизацию канала...")
    
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("SELECT product_id, description, photo_file_id FROM products")
    products = c.fetchall()
    conn.close()
    
    published_count = 0
    errors = 0
    
    for product_id, description, photo_file_id in products:
        try:
            # Проверяем, опубликован ли уже товар
            conn = sqlite3.connect('shop.db')
            c = conn.cursor()
            c.execute("SELECT published_message_id FROM products WHERE product_id = ?", (product_id,))
            message_id = c.fetchone()[0]
            conn.close()
            
            if message_id:
                # Проверяем существует ли сообщение
                try:
                    await bot.get_message(chat_id=CHANNEL_ID, message_id=message_id)
                    continue  # Сообщение существует, пропускаем
                except:
                    pass
                    
            # Публикуем товар
            message_id = await publish_to_channel(product_id, description, photo_file_id)
            if message_id:
                published_count += 1
            else:
                errors += 1
                
            await asyncio.sleep(1)  # Задержка чтобы не перегружать API
        except Exception as e:
            logger.error(f"Ошибка синхронизации товара {product_id}: {e}")
            errors += 1
    
    await message.answer(f"✅ Синхронизация завершена\n"
                         f"Опубликовано новых товаров: {published_count}\n"
                         f"Ошибок: {errors}")