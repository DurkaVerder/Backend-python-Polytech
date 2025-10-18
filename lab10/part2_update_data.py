from sqlalchemy.orm import sessionmaker
from database import engine, User, Post

# Создание сессии
Session = sessionmaker(bind=engine)

def update_user_email(username, new_email):
    """Обновление email пользователя"""
    session = Session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            old_email = user.email
            user.email = new_email
            session.commit()
            print(f"Email пользователя {username} обновлен с {old_email} на {new_email}")
        else:
            print(f"Пользователь {username} не найден")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении email: {e}")
    finally:
        session.close()

def update_post_content(post_id, new_content):
    """Обновление содержимого поста"""
    session = Session()
    try:
        post = session.query(Post).filter(Post.id == post_id).first()
        if post:
            old_content = post.content
            post.content = new_content
            session.commit()
            print(f"Содержимое поста ID {post_id} обновлено")
            print(f"Старое содержимое: {old_content[:50]}...")
            print(f"Новое содержимое: {new_content[:50]}...")
        else:
            print(f"Пост с ID {post_id} не найден")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении поста: {e}")
    finally:
        session.close()

def main():
    """Основная функция для обновления данных"""
    print("Обновление email пользователя user1...")
    update_user_email('user1', 'newemail@example.com')
    
    print("\nОбновление содержимого поста с ID 1...")
    update_post_content(1, 'Это новое обновленное содержимое первого поста')

if __name__ == "__main__":
    main()