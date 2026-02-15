"""
Имя файла: callbacks.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Обработка нажатий кнопок
"""

from loader import bot
from handlers.text_input import register_user


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """ Обработчик нажатий (callback_query_handler) """
    if call.data == "btn1_click":
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
