from exceptions import UserNotFoundError, BookNotAvailableError, PermissionDeniedError


# Шаг 1
def delete_book(books: list, role: str):
    if role != "admin":
        raise PermissionDeniedError("Access denied. Only admins can delete books.")
    if not books:
        raise ValueError("No books to delete.")
    return f"Book '{books.pop()}' deleted."


# Шаг 1
def get_book(book_id: int):
    if book_id <= 0:
        raise ValueError("Invalid book ID. Must be positive.")
    if book_id > 1000:
        raise LookupError("Book not found in database.")
    return {"id": book_id, "title": "Sample Book", "author": "Unknown"}


# Шаг 2
def get_all_books_by_author(author: str):
    try:
        if not author:
            raise ValueError("Author name cannot be empty.")
        return [
            {"id": 1, "title": "Book One", "author": author},
            {"id": 2, "title": "Book Two", "author": author},
        ]
    except Exception as e:
        print(f"An error occurred in get_all_books_by_author: {e}")
        return []


# Шаг 3
def add_book(title: str, author: str, year: int):
    try:
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        if year < 0:
            raise ValueError("Year cannot be negative.")
        return {"id": 123, "title": title, "author": author, "year": year}
    except Exception as e:
        print(f"An error occurred in add_book: {e}")
        return None
    finally:
        print("add_book function executed.")


# Шаг 4
def check_registered_user(user_id: int):
    try:
        if user_id <= 0:
            raise ValueError("Invalid user ID. Must be positive.")
        if user_id % 5 == 0:
            raise PermissionDeniedError("User is banned.")
        if user_id > 1000:
            raise UserNotFoundError("User not found.")
        return True
    except ValueError as e:
        print(f"Validation error: {e}")
        return False
    except UserNotFoundError as e:
        print(f"User error: {e}")
        return False
    except PermissionDeniedError as e:
        print(f"Permission denied error: {e}")
        return False
    finally:
        print("check_registered_user finished.")


# Шаг 4
def borrow_book(user: str, book_id: int):
    try:
        if not user:
            raise UserNotFoundError("User must be provided.")
        if book_id <= 0:
            raise ValueError("Invalid book ID.")
        if book_id % 2 == 0:
            raise BookNotAvailableError("This book is already borrowed.")
        return f"Book {book_id} borrowed by {user}."
    except UserNotFoundError as e:
        print(f"Borrow error (user): {e}")
        return None
    except ValueError as e:
        print(f"Borrow error (validation): {e}")
        return None
    except BookNotAvailableError as e:
        print(f"Borrow error (availability): {e}")
        return None
    finally:
        print("borrow_book finished.")


# Шаг 4
def update_book_info(book_id: int, title: str = None):
    try:
        if book_id <= 0:
            raise ValueError("Book ID must be positive.")
        if book_id > 500:
            raise LookupError("Book not found.")
        if title is None:
            raise AttributeError("Title must be provided for update.")
        return f"Book {book_id} updated with new title '{title}'."
    except ValueError as e:
        print(f"Update error (validation): {e}")
    except LookupError as e:
        print(f"Update error (lookup): {e}")
    except AttributeError as e:
        print(f"Update error (attribute): {e}")
    finally:
        print("update_book_info finished.")


# Шаг 5
def reserve_book(user: str, book_id: int):
    try:
        if not user:
            raise UserNotFoundError("User is required.")
        if book_id <= 0:
            raise ValueError("Book ID must be valid.")
        if book_id % 3 == 0:
            raise BookNotAvailableError("Book cannot be reserved.")
        return f"Book {book_id} reserved for {user}."
    except UserNotFoundError as e:
        print(f"Reserve error (user): {e}")
    except ValueError as e:
        print(f"Reserve error (validation): {e}")
    except BookNotAvailableError as e:
        print(f"Reserve error (availability): {e}")
    finally:
        print("reserve_book finished.")


# Шаг 7
def validate_role(role: str):
    try:
        if role != "admin":
            raise PermissionDeniedError("Only admin can perform this action.")
        return True
    except PermissionDeniedError as e:
        print(f"Permission error: {e}")
        return False
    finally:
        print("validate_role finished.")


# Шаг 8
def search_book_by_title(title: str):
    if not title:
        raise ValueError("Title cannot be empty.")
    return f"Book with title '{title}' found."


# Шаг 8
def return_book(user: str, book_id: int):
    if not user:
        raise UserNotFoundError("User required for return.")
    if book_id <= 0:
        raise ValueError("Invalid book ID.")
    return f"Book {book_id} returned by {user}."


# Шаг 8
def recommend_books(user: str, genre: str):
    if not user:
        raise UserNotFoundError("User must be logged in.")
    if not genre:
        raise ValueError("Genre must be provided.")
    return [f"{genre} Book 1", f"{genre} Book 2"]
