# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ReadingQueue
def parse_date(value):
    """Parse a date string into a datetime.date object.
    
    Supports:
    - 'YYYY-MM-DD' (ISO format)
    - 'YYYY/MM/DD'
    - 'YYYY.MM.DD'
    - 'DD/MM/YYYY'
    - 'DD-MM-YYYY'
    
    Returns None if parsing fails.
    """
    import datetime
    if value is None:
        return None
    
    value = str(value).strip()
    
    formats = [
        ('%Y-%m-%d', None),
        ('%Y/%m/%d', None),
        ('%Y.%m.%d', None),
        ('%d/%m/%Y', None),
        ('%d-%m-%Y', None),
    ]
    
    for fmt, _ in formats:
        try:
            return datetime.date.strptime(value, fmt)
        except ValueError:
            continue
    
    return None
