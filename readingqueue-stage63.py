# === Stage 63: Add relationships between records where useful ===
# Project: ReadingQueue
def link_related(records):
    by_title = {}
    for rec in records:
        by_title.setdefault(rec.get("title"), []).append(rec)

    for rec in records:
        title = rec.get("title")
        related = []
        for other in by_title.get(title, []):
            if other.get("id") != rec.get("id"):
                related.append({"type": "same_title", "id": other.get("id")})
        rec["related"] = related
        if rec.get("status") == "completed" and rec.get("rating"):
            rec["related"].append({"type": "rated_like", "id": rec.get("id")})
    return records
