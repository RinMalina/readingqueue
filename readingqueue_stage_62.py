# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ReadingQueue
def score_book(book, profile):
    """Score a book against a reader profile to recommend the best next read."""
    score = 0
    if book.get("rating") and book["rating"] >= 4:
        score += 40
    if book.get("status") == "to-read":
        score += 10
    if book.get("tags"):
        score += min(len(book["tags"]) * 5, 30)
    if book.get("pages") and book.get("read"):
        score += 20
    if book.get("completed") and book.get("rating", 0) >= 4:
        score += 30
    return score

def recommend_next(books, profile):
    """Return the best book to read next based on scoring."""
    candidates = [b for b in books if b.get("status") == "to-read"]
    if not candidates:
        return None
    best = max(candidates, key=lambda b: score_book(b, profile))
    return best

def rank_books(books):
    """Sort books by score, best first."""
    return sorted(books, key=lambda b: score_book(b, profile), reverse=True)
