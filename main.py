import telebot
from telebot import types

TOKEN = '8267818862:AAGbLX7yQXydFabIBZmXdiFGiHWLt3zfSn8'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    markup = types.InlineKeyboardMarkup()
    # Создаем кнопки
    item1 = types.InlineKeyboardButton('Кнопка1', callback_data="btn1_click")
    item2 = types.InlineKeyboardButton('Кнопка2', callback_data="btn2_click")
    item3 = types.InlineKeyboardButton('Кнопка3', callback_data="btn3_click")
    item4 = types.InlineKeyboardButton('Кнопка4', callback_data="btn4_click")
    # Добавляем кнопки в клавиатуру
    markup.add(item1, item2, item3, item4)
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=markup)


# Обработчик нажатий (callback_query_handler)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn1_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 1")
    elif call.data == "btn2_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 2")
    elif call.data == "btn3_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 3")
    elif call.data == "btn4_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 4")


bot.infinity_polling()
