# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ReadingQueue
def validate_data(records):
    warnings = []
    errors = []
    valid_ratings = set()
    for r in records:
        book = r.get("book", "")
        rating = r.get("rating")
        pages = r.get("pages")
        if not isinstance(book, str):
            errors.append("book must be a string")
        if rating is not None and (not isinstance(rating, int) or rating < 1 or rating > 5):
            warnings.append("rating out of range")
        if pages is not None and pages < 0:
            errors.append("pages cannot be negative")
    return warnings, errors
