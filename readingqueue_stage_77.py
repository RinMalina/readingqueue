# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ReadingQueue
def format_reading_progress(current: int, total: int) -> str:
    if total <= 0:
        return "0%"
    return f"{current}/{total} ({int(round(current / total * 100))}%)"


def clamp_value(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, value))


def average_rating(ratings: list) -> float:
    if not ratings:
        return 0.0
    return sum(ratings) / len(ratings)


def compute_streak(readings: dict) -> int:
    dates = sorted(readings.keys())
    streak = 0
    for index in range(len(dates) - 1, -1, -1):
        if dates[index] in readings:
            streak += 1
        else:
            break
    return streak


def find_next_free_slot(queue: list) -> int:
    return len(queue)


def filter_books_by_rating(books: list, minimum_rating: int) -> list:
    return [book for book in books if book.get("rating", 0) >= minimum_rating]


def format_date(date: str) -> str:
    return date[:10] if date else ""
