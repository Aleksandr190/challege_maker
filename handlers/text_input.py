"""
Имя файла: text_input.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Обработка текстовых ответов
"""

from loader import bot, db


def register_user(message):
    """Обработка введенного имени при регистрации """
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    entered_name = message.text

    if not db.user_exists(user_id):
        db.add_user(user_id, first_name, username, entered_name)
        bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")
    else:
        bot.send_message(message.chat.id, "Вы уже есть в базе данных.")
