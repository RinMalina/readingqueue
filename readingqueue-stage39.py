# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ReadingQueue
def repair_queue():
    """Fix simple data integrity issues in the reading queue."""
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        data = {"queue": [], "progress": {}, "ratings": {}, "streaks": {}}
    # Ensure all required keys exist
    for key in ["queue", "progress", "ratings", "streaks"]:
        if key not in data:
            data[key] = []
    # Remove duplicate entries in queue
    seen = set()
    unique_queue = []
    for entry in data["queue"]:
        if entry["title"] not in seen:
            seen.add(entry["title"])
            unique_queue.append(entry)
    data["queue"] = unique_queue
    # Ensure progress keys match queue titles
    for entry in data["queue"]:
        if entry["title"] not in data["progress"]:
            data["progress"][entry["title"]] = {"pages": 0, "total_pages": 0}
    # Ensure ratings keys match queue titles
    for entry in data["queue"]:
        if entry["title"] not in data["ratings"]:
            data["ratings"][entry["title"]] = {}
    # Ensure streaks has at least today's date
    today = datetime.date.today().strftime("%Y-%m-%d")
    if today not in data["streaks"]:
        data["streaks"][today] = 0
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print("Data repaired successfully.")
