# === Stage 73: Add a lightweight HTML report export ===
# Project: ReadingQueue
def export_html_report(db, path="reading_report.html"):
    books = db["books"]
    rows = []
    for book in books:
        rows.append("<tr><td>{}</td><td>{}</td><td>{}</td><td>{:.0%}</td><td>{}</td></tr>".format(
            book["title"], book["author"], book["status"],
            100.0 * book["progress_pages"] / book["total_pages"] if book["total_pages"] else 0.0,
            book["rating"] if book["rating"] else ""))
    streak = db["streak"]
    streak_html = "{}".format(streak["days"]) if streak else "0"
    html = "<html><head><title>ReadingQueue Report</title></head><body>"
    html += "<h1>ReadingQueue Report</h1>"
    html += "<p>Current streak: {} days</p>".format(streak_html)
    html += "<table><tr><th>Title</th><th>Author</th><th>Status</th><th>Progress</th><th>Rating</th></tr>"
    html += "".join(rows)
    html += "</table></body></html>"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
