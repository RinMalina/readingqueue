# === Stage 64: Add validation for relationship references ===
# Project: ReadingQueue
def validate_relationships(records):
    ids = {r["id"] for r in records}
    for r in records:
        if r.get("id") is None or isinstance(r["id"], str) or not isinstance(r["id"], int):
            raise ValueError(f"Record {r.get('id')} has an invalid id")
        if r.get("status") not in ("to_read", "reading", "completed"):
            raise ValueError(f"Record {r['id']} has an invalid status")
        if r.get("rating", 0) < 0 or r.get("rating", 0) > 5:
            raise ValueError(f"Record {r['id']} has an invalid rating")
        if r.get("start_date"):
            start = _parse_date(r["start_date"])
            if start is None:
                raise ValueError(f"Record {r['id']} has an invalid start_date")
            if r.get("end_date"):
                end = _parse_date(r["end_date"])
                if end is None:
                    raise ValueError(f"Record {r['id']} has an invalid end_date")
                elif start > end:
                    raise ValueError(f"Record {r['id']} end_date before start_date")
        if r.get("author_id") and r["author_id"] not in ids:
            raise ValueError(f"Record {r['id']} references unknown author_id")
        if r.get("next_id") and r["next_id"] not in ids:
            raise ValueError(f"Record {r['id']} references unknown next_id")

def _parse_date(value):
    try:
        return datetime.date.fromisoformat(value)
    except (TypeError, ValueError):
        return None
