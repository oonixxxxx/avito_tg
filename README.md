# 🛍️ Telegram Shop Bot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Aiogram Version](https://img.shields.io/badge/aiogram-3.x-blue)](https://docs.aiogram.dev/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Telegram Shop Bot - это полнофункциональный бот для создания интернет-магазина в Telegram. Бот позволяет пользователям добавлять товары с описанием и фотографиями, просматривать каталог, искать товары, а также автоматически публикует новые товары в Telegram-канале.

![Bot Interface](https://via.placeholder.com/800x400?text=Telegram+Shop+Bot+Interface)

## 🌟 Основные возможности

- 📝 Добавление товаров с описанием и фотографиями
- 🔍 Поиск товаров по описанию
- 📚 Интерактивный каталог с постраничной навигацией
- 📢 Автоматическая публикация товаров в Telegram-канале
- 👤 Личный кабинет с управлением своими товарами
- ⚙️ Административные инструменты для управления магазином
- 💾 Хранение данных в SQLite базе данных

## 🚀 Установка и запуск

### Предварительные требования
- Python 3.10 или выше
- Telegram бот (получить токен от [@BotFather](https://t.me/BotFather))
- Telegram канал (для публикации товаров)

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/telegram-shop-bot.git
cd telegram-shop-bot
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл конфигурации `.env`:
```env
BOT_TOKEN=your_bot_token_here
CHANNEL_ID=@your_channel_username
ADMIN_ID=your_telegram_id
```

4. Запустите бота:
```bash
python bot.py
```

## 📖 Команды бота

### Для пользователей
| Команда          | Описание                              |
|------------------|---------------------------------------|
| `/start`         | Начать работу с ботом                 |
| `/add`           | Добавить новый товар                  |
| `/catalog`       | Просмотреть каталог товаров           |
| `/search`        | Поиск товаров по описанию             |
| `/my_products`   | Просмотреть и управлять своими товарами |

### Для администратора
| Команда          | Описание                              |
|------------------|---------------------------------------|
| `/sync_channel`  | Синхронизировать канал с базой данных |

## 🗺️ Roadmap

### Версия 1.0 (Current)
- [x] Регистрация пользователей
- [x] Добавление товаров
- [x] Постраничный каталог
- [x] Поиск по описанию
- [x] Автоматическая публикация в канал
- [x] Управление своими товарами
- [x] Синхронизация канала

### Версия 1.1
- [ ] Система заказов
- [ ] Корзина пользователя
- [ ] Платежная интеграция
- [ ] Категории товаров
- [ ] Система рейтингов и отзывов

### Версия 2.0
- [ ] Веб-панель администратора
- [ ] Мобильное приложение
- [ ] Система аналитики
- [ ] Интеграция с CRM

## 🧾 Документация

### Структура базы данных
```mermaid
erDiagram
    users ||--o{ products : has
    products {
        integer product_id PK
        integer user_id FK
        text description
        text photo_file_id
        timestamp added_at
        integer published_message_id
    }
    users {
        integer user_id PK
        timestamp created_at
    }
```

### Файловая структура проекта
```
telegram-shop-bot/
├── bot.py                # Основной файл бота
├── requirements.txt      # Зависимости
├── .env                  # Конфигурация
├── shop.db               # База данных SQLite
├── README.md             # Документация
└── LICENSE               # Лицензия
```

### Конфигурация
Создайте файл `.env` со следующими параметрами:

| Переменная      | Описание                          | Пример              |
|-----------------|-----------------------------------|---------------------|
| `BOT_TOKEN`     | Токен Telegram бота               | `123456:ABC-DEF123` |
| `CHANNEL_ID`    | ID канала для публикации товаров  | `@my_shop_channel`  |
| `ADMIN_ID`      | ID администратора бота            | `123456789`         |

## 🛠️ Технологии

- **Python** - основной язык программирования
- **Aiogram** - фреймворк для создания Telegram ботов
- **SQLite** - база данных для хранения информации
- **Dotenv** - управление конфигурацией
- **Asyncio** - асинхронное программирование

## 🤝 Как внести вклад

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add some amazing feature'`)
4. Запушьте ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📜 Лицензия

Этот проект распространяется под лицензией MIT - подробности см. в файле [LICENSE](LICENSE).

## ✉️ Контакты

Если у вас есть вопросы или предложения, пишите:
- Email: your.email@example.com
- Telegram: @yourtelegram

---

**Telegram Shop Bot** © 2023 - Простой и функциональный магазин в Telegram!