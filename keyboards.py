"""
Имя файла: keyboards.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Кнопки
"""

from telebot import types


class StartKeyboard:
    """
       #Класс клавиатуры вызываемой при запуске бота

        Attributes:
            markup:  объект клавиатуры
    """

    def __init__(self):
        """
        Конструктор класса. Создает клавиатуру со следующими кнопками:
            - Регистрация;
            - Добавить упражнение;
            - Создать челендж;
            - Вывод информации;
        """
        # Создаем клавиатуру
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        # Создаем кнопки
        item1 = types.InlineKeyboardButton('Регистрация', callback_data="btn1_click")
        item2 = types.InlineKeyboardButton('Добавить упражнение', callback_data="btn2_click")
        item3 = types.InlineKeyboardButton('Создать челендж', callback_data="btn3_click")
        item4 = types.InlineKeyboardButton('Вывод информации', callback_data="btn4_click")
        # Добавляем кнопки в клавиатуру
        self.markup.add(item1, item2, item3, item4)
