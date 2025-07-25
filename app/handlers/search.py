from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

router = Router(name="start-router")

class SearchProduct(StatesGroup):
    waiting_query = State()

# Обработчик команды /search
@dp.message(Command("search"))
async def cmd_search(message: types.Message, state: FSMContext):
    await state.set_state(SearchProduct.waiting_query)
    await message.answer("🔍 Введите поисковый запрос:")

# Обработчик поискового запроса
@dp.message(SearchProduct.waiting_query)
async def process_search_query(message: types.Message, state: FSMContext):
    query = message.text.strip()
    if len(query) < 2:
        await message.answer("⚠️ Слишком короткий запрос. Введите минимум 2 символа.")
        return
    
    results = search_products(query)
    
    if not results:
        await message.answer("🔍 По вашему запросу ничего не найдено")
        await state.clear()
        return
    
    await message.answer(f"🔍 Найдено товаров: {len(results)}")
    
    # Отправляем первые 5 результатов (чтобы не перегружать)
    for i, (product_id, description, photo_file_id) in enumerate(results[:5], 1):
        caption = f"Результат #{i}\nID: {product_id}\nОписание: {description}"
        await message.answer_photo(
            photo=photo_file_id,
            caption=caption
        )
    
    if len(results) > 5:
        await message.answer(f"ℹ️ Показано 5 из {len(results)} результатов. Уточните запрос для более точного поиска.")
    
    await state.clear()

# Поиск похожих товаров
@dp.callback_query(F.data.startswith("similar_"))
async def similar_products_handler(callback: types.CallbackQuery):
    product_id = int(callback.data.split("_")[1])
    product = get_product_by_id(product_id)
    
    if not product:
        await callback.answer("Товар не найден")
        return
    
    _, description, _ = product
    
    # Извлекаем ключевые слова из описания
    words = re.findall(r'\w{4,}', description.lower())
    if not words:
        await callback.answer("Не удалось определить ключевые слова")
        return
    
    # Ищем по наиболее частым словам
    results = []
    for word in words[:3]:  # Берем первые 3 слова
        results.extend(search_products(word))
    
    # Убираем дубликаты
    unique_results = {r[0]: r for r in results}.values()
    
    if not unique_results:
        await callback.answer("Похожие товары не найдены")
        return
    
    await callback.answer(f"Найдено {len(unique_results)} похожих товаров")
    await callback.message.answer(f"🔍 Похожие товары ({len(unique_results)}):")
    
    # Отправляем результаты
    for i, (p_id, desc, file_id) in enumerate(unique_results[:5], 1):
        caption = f"Товар #{i}\nID: {p_id}\nОписание: {desc}"
        await callback.message.answer_photo(
            photo=file_id,
            caption=caption
        )