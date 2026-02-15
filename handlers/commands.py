"""
Имя файла: commands.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Обработка команд
"""

from loader import bot
import keyboards


@bot.message_handler(commands=['start'])
def start(message):
    """ Обработчик команды /start """
    keyboard = keyboards.StartKeyboard()
    bot.send_message(message.chat.id, "Выберите пункт меню:", reply_markup=keyboard.markup)
