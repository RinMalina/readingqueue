# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ReadingQueue
import random
from datetime import date, timedelta

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read_progress = 0  # pages read
        self.rated = None  # 1-5 stars or None
        self.started = None  # date or None

class Reader:
    def __init__(self, name):
        self.name = name
        self.current_book = None
        self.last_read_date = None
        self.read_count = 0
        self.total_pages_read = 0

class ReadingQueue:
    def __init__(self):
        self.books = {}
        self.readers = {}
        self.to_read = []
        self.reading = []
        self.completed = []
        self.readers_queue = {}

    def add_book(self, title, author, pages):
        self.books[title] = Book(title, author, pages)
        return self.books[title]

    def add_reader(self, name):
        self.readers[name] = Reader(name)
        self.readers_queue[name] = []
        return self.readers[name]

    def queue_book(self, title, reader_name):
        if reader_name in self.readers_queue:
            self.readers_queue[reader_name].append(title)
        else:
            self.to_read.append(title)

    def start_reading(self, title, reader_name, today=None):
        if today is None:
            today = date.today()
        book = self.books.get(title)
        if book and reader_name in self.readers:
            reader = self.readers[reader_name]
            reader.current_book = book
            reader.last_read_date = today
            reader.read_count += 1
            reader.total_pages_read += book.pages
            book.started = today
            self.reading.append(title)
            if title in self.readers_queue[reader_name]:
                self.readers_queue[reader_name].remove(title)

    def mark_complete(self, title, reader_name):
        reader = self.readers[reader_name]
        if reader.current_book and reader.current_book.title == title:
            reader.current_book = None
            self.completed.append(title)
            reader.last_read_date = date.today()
            return True
        return False

    def get_streak(self, reader_name):
        reader = self.readers[reader_name]
        if reader.last_read_date:
            today = date.today()
            streak = 0
            d = reader.last_read_date
            while d <= today:
                streak += 1
                d += timedelta(days=1)
            return streak
        return 0

    def get_progress(self, title):
        book = self.books.get(title)
        if book:
            return book.read_progress / book.pages * 100 if book.pages > 0 else 0
        return 0
