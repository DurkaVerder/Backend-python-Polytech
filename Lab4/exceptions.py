class UserNotFoundError(Exception):
    """Пользователь не найден."""


class BookNotAvailableError(Exception):
    """Книга недоступна для выдачи."""


class PermissionDeniedError(Exception):
    """У пользователя нет прав на выполнение действия."""
