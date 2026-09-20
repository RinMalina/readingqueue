# === Stage 42: Add CSV export without external dependencies ===
# Project: ReadingQueue
import csv
import os

def export_to_csv(queue_file, output_path):
    """Export ReadingQueue data to a CSV file without external dependencies.
    
    Args:
        queue_file: Path to the JSON file containing the ReadingQueue data.
        output_path: Path for the output CSV file.
    """
    with open(queue_file, 'r') as f:
        data = json.load(f)
    
    books = data.get('books', [])
    if not books:
        print("No books to export.")
        return
    
    fieldnames = ['title', 'author', 'status', 'progress', 'rating', 'date_added', 'date_finished']
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for book in books:
            writer.writerow({
                'title': book.get('title', ''),
                'author': book.get('author', ''),
                'status': book.get('status', ''),
                'progress': book.get('progress', 0),
                'rating': book.get('rating', 0),
                'date_added': book.get('date_added', ''),
                'date_finished': book.get('date_finished', '')
            })
    
    print(f"Exported {len(books)} books to {output_path}")
