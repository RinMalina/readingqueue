# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ReadingQueue
class SortableBook(Book):
    def __init__(self, title, author, start_date, last_update, priority):
        self.title = title
        self.author = author
        self.start_date = start_date
        self.last_update = last_update
        self.priority = priority

    def __lt__(self, other):
        return (self.title, self.start_date, self.priority, self.last_update) < (
            other.title, other.start_date, other.priority, other.last_update
        )
