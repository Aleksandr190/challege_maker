"""
Имя файла: database.py
Автор: Краюшкин А.Ю.
Дата создания: 15.02.2025
Описание: Логика работы с БД
"""

import sqlite3
from config import DEBUG
from handlers.messages import RegUserCodeMsg, AddExerciseCodeMsg


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

        # Создание таблицы упражнений "exercises"
        with self.connection:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS exercises (
                    exercise_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    exercise_name TEXT,
                    points INTEGER,
                    description TEXT
                    )
                ''')

    def user_exists(self, user_id, name):
        """Проверка, есть ли пользователь в таблице users"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "users" WHERE "user_id" = ?', (user_id,)).fetchall()
            if bool(len(result)):
                return RegUserCodeMsg.ID_ALREADY_EXISTS
            result = self.cursor.execute('SELECT * FROM "users" WHERE "entered_name" = ?', (name,)).fetchall()
            if bool(len(result)):
                return RegUserCodeMsg.NAME_ALREADY_EXISTS

        return RegUserCodeMsg.NAME_DOESNT_EXIST

    def exercise_exists(self, name):
        """Проверка, есть ли упражнение в таблице exercises"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM "exercises" WHERE "exercise_name" = ?', (name,)).fetchall()
            if bool(len(result)):
                return AddExerciseCodeMsg.NAME_ALREADY_EXISTS

        return AddExerciseCodeMsg.NAME_DOESNT_EXIST

    def add_user(self, user_id, username, first_name, entered_name):
        """Добавление нового пользователя"""
        try:
            with self.connection:
                self.cursor.execute(
                    "INSERT INTO users (user_id, first_name, username, entered_name) VALUES (?,?,?,?)",
                    (user_id, first_name, username, entered_name))
                return RegUserCodeMsg.SUCCESSFUL
        except sqlite3.Error as e:
            if DEBUG:
                print(f"Ошибка при добавлении: {e}")
            return RegUserCodeMsg.DB_ERROR

    def add_exercise(self, exercise_name, points, description):
        """Добавление нового упражнения"""
        try:
            with self.connection:
                self.cursor.execute(
                    "INSERT INTO exercises (exercise_name, points, description) VALUES (?,?,?)",
                    (exercise_name, points, description))
                return AddExerciseCodeMsg.SUCCESSFUL
        except sqlite3.Error as e:
            if DEBUG:
                print(f"Ошибка при добавлении: {e}")
            return AddExerciseCodeMsg.DB_ERROR

    def __get_column_as_list(self, table_name, column_name):
        """Получить из таблицы table_name колонку column_name и вернуть значения в ввиде списка"""
        # Выполнение запроса
        query = f"SELECT {column_name} FROM {table_name}"
        self.cursor.execute(query)

        # Получение всех строк и преобразование в список
        result = [row[0] for row in self.cursor.fetchall()]

        return result

    def get_list_exercises(self):
        """Вернуть список упражнений"""
        self.__get_column_as_list("exercises", "exercise_name")

    def close(self):
        """Закрытие соединения с БД"""
        self.connection.close()
