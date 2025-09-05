from typing import Callable, List, Dict


def welcome_message() -> str:
    return "Welcome to the system!"


def greet_user(name: str) -> str:
    return f"Hello, {name}!"


def create_user(username="Guest", role="viewer") -> Dict[str, str]:
    return {"username": username, "role": role}


def send_message(
    sender: str, recipient: str, message: str, urgent: bool = False
) -> str:
    status = "URGENT" if urgent else "normal"
    return f"[{status}] From {sender} to {recipient}: {message}"


def list_users(*users: str) -> List[str]:
    return [user for user in users]


def user_info(**info) -> str:
    return ", ".join(f"{k}: {v}" for k, v in info.items())


def announce_new_user(username: str) -> str:
    def message():
        return f"New user registered: {username}"

    return message()


def execute_function(func: Callable[[], str]) -> str:
    return func()


def repeat_function(func: Callable[[], str], times: int) -> List[str]:
    return [func() for _ in range(times)]


def call_with_username(func: Callable[[str], str], username: str) -> str:
    return func(username)


def log_user_action(username: str, action: str) -> str:
    def log_entry():
        return f"{username} performed action: {action}"

    return log_entry()


def notify_admin(user: str, message: str) -> str:
    def notification():
        return f"Notify admin: {user} -> {message}"

    return notification()


say_hello_lambda = lambda: "Hello from lambda!"


greet_lambda = lambda name: f"Hello, {name} from lambda!"


def call_lambda(func: Callable[[], str]) -> str:
    return func()


def make_greeter(name: str) -> Callable[[], str]:
    def greeter():
        return f"Hi, {name}!"

    return greeter


def make_message_logger(prefix: str) -> Callable[[str], str]:
    def logger(message: str) -> str:
        return f"[{prefix}] {message}"

    return logger


def make_user_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter
