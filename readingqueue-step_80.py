# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ReadingQueue
def format_reading_message(book):
    title = book.get("title", "Untitled")
    author = book.get("author", "unknown author")
    pages = book.get("pages", 0)
    read = book.get("pages_read", 0)
    if pages <= 0:
        return f"“{title}” by {author} — not started yet."
    if read >= pages:
        return f"“{title}” by {author} — finished! {pages} pages read."
    if read > 0:
        percent = round(read / pages * 100)
        return f"“{title}” by {author} — {percent}% complete ({read} of {pages} pages)."
    return f"“{title}” by {author} — just began reading."


def format_to_read_message(book):
    title = book.get("title", "Untitled")
    author = book.get("author", "unknown author")
    return f"To read: “{title}” by {author}."


def format_streak_message(streak):
    if streak == 0:
        return "No reading streak yet. Start reading to build one!"
    if streak == 1:
        return "Great job! You’ve read for 1 day straight."
    return f"Incredible! You’ve read for {streak} days in a row."


def format_rating_message(rating):
    if rating is None:
        return "Not rated yet."
    emoji = {1: "😢", 2: "😐", 3: "🙂", 4: "😊", 5: "🤩"}
    label = {1: "poor", 2: "fair", 3: "good", 4: "great", 5: "excellent"}
    return f"Rated {label[rating]} ({emoji[rating]}) — {rating} out of 5."
