# challege_maker
telegram-bot challege maker

challenge_maker/
├── handlers/                
│   ├── callbacks.py     # Обработка нажатий кнопок
│   ├── commands.py      # Обработка команд
│   ├── text_input.py    # Обработка текстовых ответов
├── .env                 # Конфигурационный файл
├── .gitignore           # Игнорируемых файлов и каталогов для git
├── bot_database.db      # База данных sqlite
├── config.py            # Загрузка настроек из .env
├── database.py          # Логика работы с БД
├── keyboards.py         # Кнопки
├── loader.py            # Инициализация бота и БД
├── main.py              # Точка входа (запуск bot.polling)
└── README.md            # Файл описания проекта
