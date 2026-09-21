# === Stage 44: Add backup creation for the data file ===
# Project: ReadingQueue
def backup_data_file():
    """Create a timestamped backup of the JSON data file."""
    import shutil, os, json, datetime
    data_file = "reading_data.json"
    if not os.path.exists(data_file):
        return
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"reading_data_{timestamp}.json")
    shutil.copy2(data_file, backup_path)
    print(f"Backup created: {backup_path}")
