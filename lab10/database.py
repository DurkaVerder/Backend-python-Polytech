from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///lab9.db', echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="posts")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

def add_sample_users():
    session = SessionLocal()
    try:
        users = [
            User(username='user1', email='user1@example.com', password='password1'),
            User(username='user2', email='user2@example.com', password='password2'),
            User(username='user3', email='user3@example.com', password='password3'),
            User(username='admin', email='admin@example.com', password='adminpass')
        ]
        session.add_all(users)
        session.commit()
        print("Пользователи добавлены успешно!")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()

def add_sample_posts():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        posts = [
            Post(title='Первый пост', content='Содержимое первого поста', user_id=users[0].id),
            Post(title='Второй пост', content='Содержимое второго поста', user_id=users[0].id),
            Post(title='Пост админа', content='Важное сообщение от администратора', user_id=users[3].id),
            Post(title='Третий пост', content='Содержимое третьего поста', user_id=users[1].id),
            Post(title='Четвертый пост', content='Содержимое четвертого поста', user_id=users[2].id)
        ]
        session.add_all(posts)
        session.commit()
        print("Посты добавлены успешно!")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении постов: {e}")
    finally:
        session.close()

def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        print("Все пользователи:")
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
        return users
    finally:
        session.close()

def get_all_posts_with_users():
    session = SessionLocal()
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
    session = SessionLocal()
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

def update_user_email(username, new_email):
    session = SessionLocal()
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
    session = SessionLocal()
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

def delete_post(post_id):
    session = SessionLocal()
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
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user:
            posts_count = len(user.posts)
            session.delete(user)
            session.commit()
            print(f"Пользователь '{username}' и его {posts_count} пост(ов) удалены успешно")
        else:
            print(f"Пользователь {username} не найден")
    except Exception as e:
        session.rollback()
        print(f"Ошибка при удалении пользователя: {e}")
    finally:
        session.close()

def all_operations():
    print("\n--- Создание таблиц ---")
    create_tables()
    
    print("\n--- Добавление данных ---")
    add_sample_users()
    add_sample_posts()
    
    print("\n--- Извлечение данных ---")
    get_all_users()
    get_all_posts_with_users()
    get_posts_by_user('user1')
    
    print("\n--- Обновление данных ---")
    update_user_email('user1', 'newemail@example.com')
    update_post_content(1, 'Это новое обновленное содержимое первого поста')
    
    print("\n--- Удаление данных ---")
    delete_post(2)
    delete_user_and_posts('user3')

if __name__ == "__main__":
    import os
    if os.path.exists("lab9.db"):
        os.remove("lab9.db")
    
    all_operations()