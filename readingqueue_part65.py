# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ReadingQueue
def merge_imports(existing_imports, new_imports):
    merged = []
    seen = set()
    for imp in existing_imports + new_imports:
        if imp in seen:
            continue
        seen.add(imp)
        merged.append(imp)
    return merged
