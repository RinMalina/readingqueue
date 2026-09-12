# === Stage 20: Add duplicate detection for newly created records ===
# Project: ReadingQueue
def detect_duplicate(records, new_record):
    key = (new_record['title'].lower(), new_record['author'].lower())
    for r in records:
        if r['title'].lower() == key[0] and r['author'].lower() == key[1]:
            return True
    return False
