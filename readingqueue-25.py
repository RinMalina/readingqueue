# === Stage 25: Add daily summary calculations ===
# Project: ReadingQueue
def daily_summary(records):
    """Return per-book daily stats: pages read, avg rating, completion flag."""
    summary = {}
    for r in records:
        if r.get("pages") is None:
            continue
        book = r["book_id"]
        if book not in summary:
            summary[book] = {"pages": 0, "ratings": [], "completed": False}
        summary[book]["pages"] += r["pages"]
        if r.get("rating"):
            summary[book]["ratings"].append(r["rating"])
        if r.get("completed", False):
            summary[book]["completed"] = True
    for book, s in summary.items():
        if s["ratings"]:
            s["avg_rating"] = sum(s["ratings"]) / len(s["ratings"])
        else:
            s["avg_rating"] = 0.0
    return summary
