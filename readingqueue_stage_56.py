# === Stage 56: Add compact error classes for domain failures ===
# Project: ReadingQueue
class ReadingError(Exception):
    """Base class for all domain errors in the reading tracker."""
    pass


class BookNotFoundError(ReadingError):
    """Raised when a requested book cannot be found."""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book with id '{book_id}' not found.")


class DuplicateBookError(ReadingError):
    """Raised when attempting to add a book that already exists."""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book with id '{book_id}' already exists.")


class ProgressError(ReadingError):
    """Raised when progress is set to an invalid value."""
    def __init__(self, message="Progress must be between 0 and 100."):
        self.message = message
        super().__init__(self.message)


class RatingError(ReadingError):
    """Raised when a rating is outside the allowed range."""
    def __init__(self, rating):
        self.rating = rating
        super().__init__(f"Rating must be between 1 and 5, got {rating}.")


class StreakError(ReadingError):
    """Raised when a streak update cannot be applied."""
    def __init__(self, message="Cannot update reading streak."):
        self.message = message
        super().__init__(self.message)
