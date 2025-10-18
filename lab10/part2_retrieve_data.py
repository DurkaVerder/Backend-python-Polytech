from sqlalchemy.orm import sessionmaker
from database import engine, User, Post

# Создание сессии
Session = sessionmaker(bind=engine)

def get_all_users():
    """Извлечение всех записей из таблицы Users"""
    session = Session()
    try:
        users = session.query(User).all()
        print("Все пользователи:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
        return users
    finally:
        session.close()

def get_all_posts_with_users():
    """Извлечение всех записей из таблицы Posts с информацией о пользователях"""
    session = Session()
    try:
        posts = session.query(Post).join(User).all()
        print("\nВсе посты с информацией о пользователях:")
        for post in posts:
            print(f"ID: {post.id}, Title: {post.title}, Content: {post.content[:50]}..., "
                  f"Author: {post.user.username}")
        return posts
    finally:
        session.close()

def get_posts_by_user(username):
    """Извлечение записей из таблицы Posts конкретного пользователя"""
    session = Session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            posts = session.query(Post).filter(Post.user_id == user.id).all()
            print(f"\nПосты пользователя {username}:")
            for post in posts:
                print(f"ID: {post.id}, Title: {post.title}, Content: {post.content[:50]}...")
            return posts
        else:
            print(f"Пользователь {username} не найден")
            return []
    finally:
        session.close()

def main():
    """Основная функция для извлечения данных"""
    get_all_users()
    get_all_posts_with_users()
    get_posts_by_user('user1')

if __name__ == "__main__":
    main()