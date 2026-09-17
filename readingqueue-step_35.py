# === Stage 35: Add active user switching and user-specific records ===
# Project: ReadingQueue
class User:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self.books = {}  # {id: BookRecord}

    def add_book(self, book_id, book, status="to_read"):
        record = BookRecord(book_id, book, self, status)
        self.books[book_id] = record
        return record

    @property
    def active(self):
        return self.books

    @property
    def read(self):
        return [r for r in self.books.values() if r.status == "read"]

    @property
    def rated(self):
        return [r for r in self.books.values() if r.status == "read" and r.rating]

    def current_streak(self):
        streak = 0
        today = date.today()
        for day in reversed(range((today - today.weekday()).date(), today.date() + 1)):
            if day.weekday() >= 5:
                break
            if self.books and self.books.values()[0].read_date == day:
                streak += 1
            else:
                break
        return streak
