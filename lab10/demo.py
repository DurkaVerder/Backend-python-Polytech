"""
Демонстрация выполнения всех частей задания

Этот файл последовательно выполняет все части задания:
1. Создание таблиц
2. Добавление данных
3. Извлечение данных
4. Обновление данных
5. Удаление данных
"""

import os
import sys

def run_part1():
    """Часть 1: Создание таблиц"""
    print("=" * 50)
    print("ЧАСТЬ 1: СОЗДАНИЕ ТАБЛИЦ")
    print("=" * 50)
    
    from part1_create_tables import main
    main()

def run_part2():
    """Часть 2: Взаимодействие с базой данных"""
    print("\n" + "=" * 50)
    print("ЧАСТЬ 2: ВЗАИМОДЕЙСТВИЕ С БАЗОЙ ДАННЫХ")
    print("=" * 50)
    
    # Добавление данных
    print("\n--- Добавление данных ---")
    from part2_add_data import main as add_main
    add_main()
    
    # Извлечение данных
    print("\n--- Извлечение данных ---")
    from part2_retrieve_data import main as retrieve_main
    retrieve_main()
    
    # Обновление данных
    print("\n--- Обновление данных ---")
    from part2_update_data import main as update_main
    update_main()
    
    # Удаление данных
    print("\n--- Удаление данных ---")
    from part2_delete_data import main as delete_main
    delete_main()

def run_part3_info():
    """Часть 3: Информация о веб-приложении"""
    print("\n" + "=" * 50)
    print("ЧАСТЬ 3: ВЕБ-ПРИЛОЖЕНИЕ")
    print("=" * 50)
    
    print("""
Веб-приложение создано в файле main.py

Для запуска веб-приложения выполните команду:
    python main.py

Или:
    uvicorn main:app --reload

Приложение будет доступно по адресу: http://127.0.0.1:8000

Возможности веб-приложения:
- Главная страница: /
- Список пользователей: /users
- Создание пользователя: /users/create
- Редактирование пользователя: /users/{id}/edit
- Удаление пользователя: /users/{id}/delete
- Список постов: /posts
- Создание поста: /posts/create
- Редактирование поста: /posts/{id}/edit
- Удаление поста: /posts/{id}/delete

Все CRUD-операции реализованы с веб-интерфейсом.
    """)

def main():
    """Основная функция для демонстрации всех частей"""
    # Удаляем существующую базу данных для чистой демонстрации
    if os.path.exists("lab10.db"):
        os.remove("lab10.db")
        print("Существующая база данных удалена для чистой демонстрации")
    
    try:
        run_part1()
        run_part2()
        run_part3_info()
        
        print("\n" + "=" * 50)
        print("ВСЕ ЧАСТИ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Ошибка при выполнении: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()