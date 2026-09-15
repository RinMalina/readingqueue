# === Stage 28: Add overdue item detection based on due dates ===
# Project: ReadingQueue
import datetime
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ReadingItem:
    title: str
    author: str
    added_date: Optional[datetime.date] = None
    due_date: Optional[datetime.date] = None
    status: str = "to_read"  # to_read, in_progress, completed


class ReadingQueue:
    def __init__(self):
        self.items: List[ReadingItem] = []

    def add_item(self, title: str, author: str, due_date=None) -> ReadingItem:
        item = ReadingItem(title=title, author=author, due_date=due_date)
        self.items.append(item)
        return item

    def get_overdue_items(self) -> List[ReadingItem]:
        today = datetime.date.today()
        overdue = [
            item
            for item in self.items
            if item.due_date is not None and item.due_date < today and item.status != "completed"
        ]
        return overdue

    def mark_overdue(self, item: ReadingItem) -> None:
        if item.status != "completed":
            item.status = "overdue"
