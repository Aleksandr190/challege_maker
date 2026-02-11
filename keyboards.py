from telebot import types

# Класс клавиатуры вызываемой при запуске бота
class StartKeyboard:
    def __init__(self):
        # Создаем клавиатуру
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        item1 = types.InlineKeyboardButton('Регистрация', callback_data="btn1_click")
        item2 = types.InlineKeyboardButton('Добавить упражнение', callback_data="btn2_click")
        item3 = types.InlineKeyboardButton('Создать челендж', callback_data="btn3_click")
        item4 = types.InlineKeyboardButton('Вывод информации', callback_data="btn4_click")
        # Добавляем кнопки в клавиатуру
        self.markup.add(item1, item2, item3, item4)