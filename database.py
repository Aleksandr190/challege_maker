"""
Имя файла: database.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Логика работы с БД
"""

import sqlite3


class Database:
    """
        Класс логики работы с базой данных sqlite.

        Attributes:
            connection:  объект подключения к базе данных SQLite
            cursor: объект курсора, связанный с соединением self.connection
    """

    def __init__(self, db_file):
        """
        Конструктор класса. Подключается к созданной БД или создает новую БД c следующими таблицами:
            - таблица пользователей;
        """
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

        # Создание таблицы пользователей "users"
        with self.connection:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    entered_name TEXT
                )
                ''')

    def user_exists(self, user_id):
        """Проверка, есть ли пользователь в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id, username, first_name, entered_name):
        """Добавление нового пользователя"""
        with self.connection:
            # return self.cursor.execute('INSERT INTO "users" ("user_id") VALUES (?)', (user_id,))
            return self.cursor.execute(
                "INSERT INTO users (user_id, first_name, username, entered_name) VALUES (?,?,?,?)",
                (user_id, first_name, username, entered_name))

    def close(self):
        """Закрытие соединения с БД"""
        self.connection.close()
