from sqlalchemy.orm import sessionmaker
from database import engine, User, Post

# Создание сессии
Session = sessionmaker(bind=engine)

def delete_post(post_id):
    """Удаление поста по ID"""
    session = Session()
    try:
        post = session.query(Post).filter(Post.id == post_id).first()
        if post:
            title = post.title
            session.delete(post)
            session.commit()
            print(f"Пост '{title}' с ID {post_id} удален успешно")
        else:
            print(f"Пост с ID {post_id} не найден")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении поста: {e}")
    finally:
        session.close()

def delete_user_and_posts(username):
    """Удаление пользователя и всех его постов"""
    session = Session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            posts_count = len(user.posts)
            session.delete(user)  # Каскадное удаление постов происходит автоматически
            session.commit()
            print(f"Пользователь '{username}' и его {posts_count} пост(ов) удалены успешно")
        else:
            print(f"Пользователь {username} не найден")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении пользователя: {e}")
    finally:
        session.close()

def main():
    """Основная функция для удаления данных"""
    print("Удаление поста с ID 2...")
    delete_post(2)
    
    print("\nУдаление пользователя user3 и всех его постов...")
    delete_user_and_posts('user3')

if __name__ == "__main__":
    main()