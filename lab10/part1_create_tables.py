from database import create_tables

def main():
    """Программа для создания таблиц в базе данных SQLite"""
    print("Создание таблиц Users и Posts...")
    create_tables()
    print("Таблицы созданы успешно!")

if __name__ == "__main__":
    main()