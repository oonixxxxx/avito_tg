from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import sqlite3

router = Router(name="add-router")


# Создаем обьект состояния для FSM
class AddProduct(StatesGroup):
    waiting_description = State()
    waiting_photo = State()

# Обработчик команды /add
@router.message(Command("add"))
async def cmd_add(message: types.Message, state: FSMContext):
    await state.set_state(AddProduct.waiting_description)
    await message.answer("✍️ Введите описание товара и цену на товар:")

# Обработчик текста (описание товара)
@router.message(AddProduct.waiting_description)
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddProduct.waiting_photo)
    await message.answer("📸 Теперь отправьте фото товара")

# Обработчик фото товара
@router.message(AddProduct.waiting_photo, F.photo)
async def process_photo(message: types.Message, state: FSMContext):
    # Сохраняем file_id самого большого варианта фото
    photo_file_id = message.photo[-1].file_id
    
    # Получаем данные из состояния
    data = await state.get_data()
    description = data.get('description', '')
    user_id = message.from_user.id
    
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    
    try:
        # Добавляем товар в базу
        c.execute('''INSERT INTO products (user_id, description, photo_file_id)
                     VALUES (?, ?, ?)''', (user_id, description, photo_file_id))
        conn.commit()
        
        await message.answer("✅ Товар успешно добавлен!")
        
        # Показываем добавленный товар
        await message.answer_photo(
            photo=photo_file_id,
            caption=f"Описание: {description}"
        )
    
    except Exception as e:
        print(f"Ошибка добавления товара: {e}")
        await message.answer("❌ Не удалось добавить товар")
    
    finally:
        conn.close()
        await state.clear()