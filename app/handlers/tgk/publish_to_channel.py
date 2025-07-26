from app.config import BOT_TOKEN, CHANNEL_ID
from aiogram import Bot, Dispatcher
from app.handlers.functions.all_functions import update_published_message

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Публикация товара в канале
async def publish_to_channel(product_id, description, photo_file_id):
    try:
        message = await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo_file_id,
            caption=f"🆕 Новый товар!\n\n{description}\n\nID: {product_id}"
        )
        update_published_message(product_id, message.message_id)
        return message.message_id
    except Exception as e:
        print(f"Ошибка публикации в канал: {e}")
        return None