"""
Имя файла: main.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Точка входа (запуск bot.polling)
"""

from loader import bot
import handlers.commands
import handlers.text_input
import handlers.callbacks

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
