"""
Имя файла: callbacks.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Обработка нажатий кнопок
"""

from loader import bot
# from handlers.text_input import register_user
from handlers.messages import RegUserCodeMsg, AddExerciseCodeMsg, reg_messages, exercise_messages
from handlers.commands import BotStates


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """ Обработчик нажатий (callback_query_handler) """
    if call.data == "btn1_click":
        # 1. Меняем состояние FSM на BotStates.input_name и отправляем пользователю запрос на ввод своего имени
        bot.set_state(call.from_user.id, BotStates.input_name, call.message.chat.id)
        bot.send_message(call.message.chat.id, reg_messages[RegUserCodeMsg.INPUT_NAME])
    elif call.data == "btn2_click":
        # 2. Меняем состояние FSM на BotStates.input_exercise_name и отправляем пользователю запрос на ввод названия упражнения
        bot.set_state(call.from_user.id, BotStates.input_exercise_name, call.message.chat.id)
        bot.send_message(call.message.chat.id, exercise_messages[AddExerciseCodeMsg.INPUT_NAME])
    elif call.data == "btn3_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 3")
    elif call.data == "btn4_click":
        bot.answer_callback_query(call.id, "Нажата Кнопка 4")

    # Убираем "часики" с кнопки
    bot.answer_callback_query(call.id)
