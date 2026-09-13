# === Stage 24: Add grouped summaries by category or status ===
# Project: ReadingQueue
def summarize_queue(queue: list[dict]) -> dict[str, dict]:
    """Group queue entries by status and return a compact summary."""
    groups = {"to_read": [], "reading": [], "completed": [], "abandoned": []}
    for entry in queue:
        status = entry.get("status", "to_read")
        groups[status].append(entry)

    summary = {}
    for status, entries in groups.items():
        if not entries:
            continue
        total_pages = sum(e.get("pages_read", 0) for e in entries)
        total_pages_target = sum(e.get("pages", 0) for e in entries)
        progress = (total_pages / total_pages_target * 100) if total_pages_target else 0
        avg_rating = sum(e.get("rating", 0) for e in entries) / len(entries) if entries else 0
        summary[status] = {
            "count": len(entries),
            "total_pages": total_pages,
            "total_pages_target": total_pages_target,
            "progress_pct": round(progress, 1),
            "avg_rating": round(avg_rating, 1),
            "books": [e.get("title", "Unknown") for e in entries],
        }
    return summary
