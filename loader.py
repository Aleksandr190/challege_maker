"""
Имя файла: loader.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Инициализация бота и БД
"""

import telebot
import database
from config import TOKEN, DATABASE_NAME

# Инициализация бота
bot = telebot.TeleBot(TOKEN)
# Инициализация базы данных
db = database.Database(DATABASE_NAME)
