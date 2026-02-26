"""
Имя файла: commands.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Обработка команд и состояний
Для пошагового сбора данных используется  машина состояний FSM( Finite State Machine)
"""

from config import DEBUG
from loader import bot, db
from telebot.handler_backends import State, StatesGroup
from handlers.messages import RegUserCodeMsg, AddExerciseCodeMsg, reg_messages, exercise_messages
import keyboards


# Определение состояний
class BotStates(StatesGroup):
    main_menu = State()  # Состояние главного меню
    input_name = State()  # Состояние ввода имени
    input_exercise_name = State()  # Состояние ввода наименования упражнения
    input_exercise_desc = State()  # Состояние ввода описания упражнения


@bot.message_handler(commands=['start'])
def start(message):
    """ Обработчик команды /start """
    bot.set_state(message.from_user.id, BotStates.main_menu, message.chat.id)
    keyboard = keyboards.StartKeyboard()
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=keyboard.markup)


@bot.message_handler(state=BotStates.input_name)
def get_name(message):
    """ Обработчик состояния input_name """
    # В случае если диалог будет продолжен:
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    # data['name'] = message.text
    if DEBUG:
        print(f"Переключение состояния в {bot.get_state(message.from_user.id, message.chat.id)}")
        print(f"Вызван обработчик  get_name")

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    entered_name = message.text

    result_code = db.user_exists(user_id, entered_name)

    if result_code == RegUserCodeMsg.NAME_DOESNT_EXIST:
        result_code = db.add_user(user_id, first_name, username, entered_name)

    bot.send_message(message.chat.id, reg_messages[result_code])
    bot.delete_state(message.chat.id)


@bot.message_handler(state=BotStates.input_exercise_name)
def get_exercise_name(message):
    """ Обработчик состояния input_exercise_name """
    if DEBUG:
        print(f"Переключение состояния в {bot.get_state(message.from_user.id, message.chat.id)}")
        print(f"Вызван обработчик  get_exercise_name")

    entered_name = message.text
    result_code = db.exercise_exists(entered_name)

    if result_code == AddExerciseCodeMsg.NAME_DOESNT_EXIST:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = entered_name
        bot.set_state(message.from_user.id, BotStates.input_exercise_desc, message.chat.id)
        bot.send_message(message.chat.id, exercise_messages[AddExerciseCodeMsg.INPUT_DESC])
    else:
        bot.send_message(message.chat.id, exercise_messages[result_code])


@bot.message_handler(state=BotStates.input_exercise_desc)
def get_exercise_desc(message):
    """ Обработчик состояния input_exercise_name """
    if DEBUG:
        print(f"Переключение состояния в {bot.get_state(message.from_user.id, message.chat.id)}")
        print(f"Вызван обработчик  get_exercise_desc")

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['desc'] = message.text
    result_code = db.add_exercise(data['name'], data['desc'])
    bot.send_message(message.chat.id, exercise_messages[result_code])
    bot.delete_state(message.chat.id)
