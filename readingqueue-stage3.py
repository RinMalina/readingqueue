# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ReadingQueue
import re
from typing import List, Optional


def _is_positive_int(value) -> bool:
    return isinstance(value, int) and value > 0


def _is_non_negative_int(value) -> bool:
    return isinstance(value, int) and value >= 0


def _is_non_empty_string(value) -> bool:
    return isinstance(value, str) and len(value.strip()) > 0


def _is_short_string(value, max_length: int = 200) -> bool:
    if not _is_non_empty_string(value):
        return False
    return len(value.strip()) <= max_length


def _is_valid_id(value) -> bool:
    if not _is_non_empty_string(value):
        return False
    return re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', value) is not None


def _is_valid_date(value) -> bool:
    if not _is_non_empty_string(value):
        return False
    return re.fullmatch(r'\d{4}-\d{2}-\d{2}', value) is not None


def _is_valid_number(value) -> bool:
    if not _is_non_empty_string(value):
        return False
    return re.fullmatch(r'\d+(\.\d+)?', value) is not None


def validate_book_id(book_id: str) -> bool:
    return _is_valid_id(book_id)


def validate_user_id(user_id: str) -> bool:
    return _is_valid_id(user_id)


def validate_date(date_str: str) -> bool:
    return _is_valid_date(date_str)


def validate_rating(rating: float) -> bool:
    if not _is_valid_number(rating):
        return False
    return 1.0 <= float(rating) <= 5.0


def validate_progress(progress: float) -> bool:
    if not _is_valid_number(progress):
        return False
    return 0.0 <= float(progress) <= 100.0


def validate_short_text(value: str, max_length: int = 200) -> bool:
    return _is_short_string(value, max_length)


def validate_book_fields(
    title: str,
    author: str,
    book_id: str,
    user_id: str,
    date: str,
    rating: float = 0.0,
    progress: float = 0.0,
) -> bool:
    return (
        _is_non_empty_string(title)
        and _is_non_empty_string(author)
        and validate_book_id(book_id)
        and validate_user_id(user_id)
        and validate_date(date)
        and validate_rating(rating)
        and validate_progress(progress)
    )
