# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ReadingQueue
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class ReadingStatus:
    STATUS_TO_READ: str = "to_read"
    STATUS_IN_PROGRESS: str = "in_progress"
    STATUS_COMPLETED: str = "completed"
    STATUS_DROPPED: str = "dropped"

@dataclass
class Book:
    title: str
    author: str
    isbn: Optional[str] = None
    cover_url: Optional[str] = None
    notes: str = ""
    tags: List[str] = field(default_factory=list)

@dataclass
class ReadingEntry:
    book: Book
    status: str = ReadingStatus.STATUS_TO_READ
    progress_percent: float = 0.0
    rating: Optional[int] = None  # 1-5
    start_date: Optional[str] = None
    completion_date: Optional[str] = None
    pages_read: int = 0
    total_pages: int = 0
    streak_days: int = 0
    streak_last_read: Optional[str] = None
