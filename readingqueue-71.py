# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ReadingQueue
def seed_demo_data():
    if 'demo' in DATA:
        return
    DATA['demo'] = {
        'queue': [
            {'id': 'q1', 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'pages': 310, 'added': '2024-01-05'},
            {'id': 'q2', 'title': 'Project Hail Mary', 'author': 'Andy Weir', 'pages': 476, 'added': '2024-02-10'},
            {'id': 'q3', 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'pages': 443, 'added': '2024-03-20'},
        ],
        'reading': [
            {'id': 'r1', 'book_id': 'q1', 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'pages': 310, 'started': '2024-04-01', 'current_page': 245, 'rating': 5},
            {'id': 'r2', 'book_id': 'q2', 'title': 'Project Hail Mary', 'author': 'Andy Weir', 'pages': 476, 'started': '2024-04-15', 'current_page': 476, 'rating': 4},
        ],
        'completed': [
            {'id': 'c1', 'book_id': 'q3', 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'pages': 443, 'finished': '2024-03-25', 'rating': 5},
        ],
        'streak': {'current': 12, 'longest': 21, 'last_read': '2024-04-18'}
    }
