from enum import Enum

# Сообщения выводимые в чат при регистрации пользователя
class RegUserCodeMsg(Enum):
    ID_ALREADY_EXISTS = 1
    NAME_ALREADY_EXISTS = 2
    INPUT_NAME = 3
    NAME_DOESNT_EXIST = 4
    DB_ERROR = 5
    SUCCESSFUL = 6

reg_messages = {
    RegUserCodeMsg.ID_ALREADY_EXISTS: "Пользователь с таким ID уже существует.",
    RegUserCodeMsg.NAME_ALREADY_EXISTS: "Пользователь с таким именем уже существует.",
    RegUserCodeMsg.INPUT_NAME: "Пожалуйста, введите ваше имя:",
    RegUserCodeMsg.DB_ERROR: "Ошибка при взаимодействии с базой данных",
    RegUserCodeMsg.SUCCESSFUL: "Вы успешно зарегистрированы!",
}

# Сообщения выводимые в чат при добавлении упражнения
class AddExerciseCodeMsg(Enum):
    NAME_ALREADY_EXISTS = 1
    INPUT_NAME = 2
    INPUT_DESC = 3
    NAME_DOESNT_EXIST = 4
    DB_ERROR = 5
    SUCCESSFUL = 6


exercise_messages = {
    AddExerciseCodeMsg.NAME_ALREADY_EXISTS: "Упражнение с таким названием уже существует.",
    AddExerciseCodeMsg.INPUT_NAME: "Пожалуйста, введите название упражнения:",
    AddExerciseCodeMsg.INPUT_DESC: "Пожалуйста, введите краткое описание упражнения:",
    AddExerciseCodeMsg.DB_ERROR: "Ошибка при взаимодействии с базой данных",
    AddExerciseCodeMsg.SUCCESSFUL: "Упражнение успешно добавленно!",
}
