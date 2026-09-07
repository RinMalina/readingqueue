# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ReadingQueue
def format_queue_entry(book: dict) -> str:
    status = book.get("status", "unknown")
    progress = book.get("progress", 0)
    pages = book.get("total_pages", 0)
    pct = progress / pages * 100 if pages else 0
    stars = book.get("rating", 0)
    line = f"{book['title'][:40]:40s}"
    if status == "reading":
        bar = progress / pages * 40
        bar = int(bar)
        bar = bar * "#" + (40 - bar) * "."
        line += f" | {bar}"
    else:
        line += f" | {'📖' if status == 'to_read' else '✅'}"
    line += f" | {pct:5.1f}% | {'⭐' * stars}"
    return line

def format_progress_report(books: list, streak_days: int) -> str:
    total = len(books)
    active = sum(1 for b in books if b.get("status") == "reading")
    finished = sum(1 for b in books if b.get("status") == "finished")
    reading = sum(1 for b in books if b.get("status") == "to_read")
    lines = [f"📚 Reading Queue Report", f"{'─' * 40}",
             f"Total books: {total}",
             f"To read: {reading}",
             f"Reading: {active}",
             f"Finished: {finished}",
             f"Reading streak: {streak_days} days"]
    return "\n".join(lines)
