"""
Имя файла: loader.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Инициализация бота и БД
"""
import telebot
from telebot import types
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

import database
from config import TOKEN, DATABASE_NAME

# Инициализация бота
bot = telebot.TeleBot(TOKEN, state_storage=StateMemoryStorage())
bot.add_custom_filter(custom_filters.StateFilter(bot))
# Инициализация базы данных
db = database.Database(DATABASE_NAME)
