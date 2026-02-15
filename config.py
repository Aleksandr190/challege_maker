"""
Имя файла: config.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Загрузка настроек из .env
"""

import os
from dotenv import load_dotenv

load_dotenv()
# Токен Telegram-бота
TOKEN = os.getenv("BOT_TOKEN")
# Наименование базы данных
DATABASE_NAME = os.getenv("DB_NAME")