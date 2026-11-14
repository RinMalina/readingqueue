# === Stage 72: Add Markdown report export ===
# Project: ReadingQueue
def export_markdown(data, path):
    books = data.get("books", [])
    streak = data.get("streak", 0)
    lines = ["# ReadingQueue Report", ""]
    lines.append(f"Current Streak: {streak} day(s)")
    lines.append("")
    lines.append("## To-Read")
    to_read = [b for b in books if b.get("status") == "to-read"]
    if to_read:
        for b in to_read:
            lines.append(f"- {b.get('title')} by {b.get('author')}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## In Progress")
    in_progress = [b for b in books if b.get("status") == "reading"]
    if in_progress:
        for b in in_progress:
            pages = b.get("pages", {})
            cur = pages.get("current", 0)
            tot = pages.get("total", 0)
            pct = round(cur / tot * 100) if tot else 0
            lines.append(f"- {b.get('title')} by {b.get('author')} ({cur}/{tot}, {pct}%)")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Completed")
    completed = [b for b in books if b.get("status") == "completed"]
    if completed:
        for b in completed:
            rating = b.get("rating", 0)
            pages = b.get("pages", {})
            tot = pages.get("total", 0)
            lines.append(f"- {b.get('title')} by {b.get('author')} (pages={tot}, rating={rating})")
    else:
        lines.append("- None")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
