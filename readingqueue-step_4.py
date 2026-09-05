# === Stage 4: Implement create operations for the primary records ===
# Project: ReadingQueue
def create_book(self, title: str, author: str, isbn: str, year: str | None = None) -> Book:
    return Book(title, author, isbn, year)

def create_category(self, name: str) -> Category:
    return Category(name)

def create_reading_goal(self, target: int, start_date: str | None = None, end_date: str | None = None) -> ReadingGoal:
    return ReadingGoal(target, start_date, end_date)

def create_reading_streak(self, book: Book, start_date: str, end_date: str) -> ReadingStreak:
    return ReadingStreak(book, start_date, end_date)

def create_reading_record(self, book: Book, start_date: str, end_date: str, pages_read: int, rating: int) -> ReadingRecord:
    return ReadingRecord(book, start_date, end_date, pages_read, rating)

def create_reading_queue(self, book: Book, status: str, priority: int = 0) -> ReadingQueue:
    return ReadingQueue(book, status, priority)
