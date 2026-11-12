# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ReadingQueue
def generate_changelog(activity_log, max_entries=10):
    """Build a compact changelog from the activity log."""
    grouped = {}
    for entry in activity_log:
        date = entry.get('date')
        if not date:
            continue
        grouped.setdefault(date, []).append(entry)

    lines = []
    for date in sorted(grouped.keys(), reverse=True):
        lines.append('# ' + date)
        for entry in grouped[date][-max_entries:]:
            action = entry.get('type', 'entry').title()
            title = entry.get('title', 'Unknown')
            lines.append('- ' + action + ': ' + title)

    return '\n'.join(lines)


def load_activity_log(path='activity_log.json'):
    """Load the activity log from a JSON file."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_changelog(changelog, path='changelog.md'):
    """Write the changelog to a markdown file."""
    with open(path, 'w', encoding='utf-8') as file:
        file.write(changelog)


def rebuild_changelog():
    """Regenerate and persist the changelog from the activity log."""
    log = load_activity_log()
    changelog = generate_changelog(log)
    save_changelog(changelog)
    return changelog
