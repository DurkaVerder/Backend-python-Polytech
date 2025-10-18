from sqlalchemy.orm import sessionmaker
from database import engine, User, Post

# Создание сессии
Session = sessionmaker(bind=engine)

def add_users():
    """Добавление пользователей в таблицу Users"""
    session = Session()
    try:
        # Создание нескольких пользователей
        users = [
            User(username='user1', email='user1@example.com', password='password1'),
            User(username='user2', email='user2@example.com', password='password2'),
            User(username='user3', email='user3@example.com', password='password3'),
            User(username='admin', email='admin@example.com', password='adminpass')
        ]
        
        # Добавление пользователей в сессию
        session.add_all(users)
        session.commit()
        print("Пользователи добавлены успешно!")
        
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()

def add_posts():
    """Добавление постов в таблицу Posts"""
    session = Session()
    try:
        # Получаем всех пользователей
        users = session.query(User).all()
        
        # Создание постов для разных пользователей
        posts = [
            Post(title='Первый пост', content='Содержимое первого поста', user_id=users[0].id),
            Post(title='Второй пост', content='Содержимое второго поста', user_id=users[0].id),
            Post(title='Пост админа', content='Важное сообщение от администратора', user_id=users[3].id),
            Post(title='Третий пост', content='Содержимое третьего поста', user_id=users[1].id),
            Post(title='Четвертый пост', content='Содержимое четвертого поста', user_id=users[2].id)
        ]
        
        # Добавление постов в сессию
        session.add_all(posts)
        session.commit()
        print("Посты добавлены успешно!")
        
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении постов: {e}")
    finally:
        session.close()

def main():
    """Основная функция для добавления данных"""
    print("Добавление пользователей...")
    add_users()
    
    print("\nДобавление постов...")
    add_posts()

if __name__ == "__main__":
    main()