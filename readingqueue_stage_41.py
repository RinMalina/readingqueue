# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ReadingQueue
def import_from_plain_text(filepath):
    """Import books from a simple line-based text file.
    
    Expected format:
        Title, Author, Year
        Another Book, Another Author, 2020
    """
    books = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return books

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 2:
            continue
        title = parts[0].strip()
        author = parts[1].strip()
        year = parts[2].strip() if len(parts) > 2 else ''
        books.append({'title': title, 'author': author, 'year': year})

    return books
