from others import *


def run_all():
    print("--- Step 1 ---")
    try:
        print(delete_book(["Book1"], "admin"))
        print(get_book(10))
    except Exception as e:
        print(f"Step 1 error in run_all: {e}")

    print("\n--- Step 2 ---")
    print(get_all_books_by_author("Tamerlan"))

    print("\n--- Step 3 ---")
    print(add_book("Go", "Pablo", 1991))

    print("\n--- Step 4 ---")
    check_registered_user(10)
    print(borrow_book("Alex", 3))
    print(update_book_info(100, "New Title"))

    print("\n--- Step 5 ---")
    print(reserve_book("Alex", 7))

    print("\n--- Step 7 ---")
    validate_role("viewer")

    print("\n--- Step 8 ---")
    try:
        print(search_book_by_title("Python Advanced"))
        print(return_book("Nikita", 42))
        print(recommend_books("Semes", "Fantasy"))
    except Exception as e:
        print(f"Step 8 error in run_all: {e}")


if __name__ == "__main__":
    run_all()
