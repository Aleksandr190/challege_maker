import telebot
import sqlite3
import keyboards
import database

from telebot import types

TOKEN = '8267818862:AAGbLX7yQXydFabIBZmXdiFGiHWLt3zfSn8'

bot = telebot.TeleBot(TOKEN)

db = database.Database("bot_database.db")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = keyboards.StartKeyboard()
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=keyboard.markup)


# Обработчик нажатий (callback_query_handler)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn1_click":
        #bot.answer_callback_query(call.id, "Нажата Кнопка 1")
        # 1. Отправляем пользователю запрос на ввод
        msg = bot.send_message(call.message.chat.id, "Пожалуйста, введите ваше имя:")
        # 2. Переходим к следующему шагу — ожиданию текста
        # Мы передаем сообщение 'msg' и функцию, которая обработает ответ
        bot.register_next_step_handler(msg, register_user)
    elif call.data == "btn2_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 2")
    elif call.data == "btn3_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 3")
    elif call.data == "btn4_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 4")

    # Убираем "часики" с кнопки
    bot.answer_callback_query(call.id)

# 3. Прием данных
def register_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    entered_name = message.text

    if not db.user_exists(user_id):
        db.add_user(user_id, first_name, username, entered_name)
        bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")
    else:
        bot.send_message(message.chat.id, "Вы уже есть в базе данных.")

bot.infinity_polling()
