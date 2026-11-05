# === Stage 57: Add structured result objects for command handlers ===
# Project: ReadingQueue
class Book:
    def __init__(self, title, author, status="to_read", pages_total=0, pages_read=0, rating=0):
        self.title = title
        self.author = author
        self.status = status
        self.pages_total = pages_total
        self.pages_read = pages_read
        self.rating = rating

    def __repr__(self):
        return f"Book(title={self.title!r}, status={self.status!r}, pages={self.pages_read}/{self.pages_total}, rating={self.rating})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "status": self.status, "pages_total": self.pages_total, "pages_read": self.pages_read, "rating": self.rating}


class ReadingStats:
    def __init__(self, books):
        self.books = books

    def to_read_count(self):
        return sum(1 for b in self.books if b.status == "to_read")

    def reading_count(self):
        return sum(1 for b in self.books if b.status == "reading")

    def finished_count(self):
        return sum(1 for b in self.books if b.status == "finished")

    def average_rating(self):
        rated = [b.rating for b in self.books if b.rating > 0]
        return round(sum(rated) / len(rated), 2) if rated else 0


class StreakResult:
    def __init__(self, days, last_read_date, current_book):
        self.days = days
        self.last_read_date = last_read_date
        self.current_book = current_book

    def to_dict(self):
        return {"days": self.days, "last_read_date": self.last_read_date, "current_book": self.current_book}


class RatingResult:
    def __init__(self, book, rating):
        self.book = book
        self.rating = rating

    def to_dict(self):
        return {"book": self.book.to_dict(), "rating": self.rating}


class ProgressResult:
    def __init__(self, book, percent, pages_read, pages_total):
        self.book = book
        self.percent = percent
        self.pages_read = pages_read
        self.pages_total = pages_total

    def to_dict(self):
        return {"book": self.book.to_dict(), "percent": self.percent, "pages_read": self.pages_read, "pages_total": self.pages_total}
