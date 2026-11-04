# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ReadingQueue
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_black": "\033[40m",
}

COLORS = {
    "title": ANSI["bold"] + ANSI["cyan"],
    "header": ANSI["bold"] + ANSI["magenta"],
    "queue": ANSI["yellow"],
    "reading": ANSI["green"],
    "done": ANSI["cyan"],
    "star": ANSI["yellow"],
    "empty": ANSI["white"],
    "streak": ANSI["red"] + ANSI["bold"],
    "info": ANSI["blue"],
}


def colorize(text, color):
    if not colors_enabled:
        return text
    return f"{COLORS[color]}{text}{ANSI['reset']}"


def banner(title):
    print()
    print(colorize(title, "title"))
    print(colorize("=" * len(title), "header"))


def print_book(book):
    status = {
        "to_read": "queue",
        "reading": "reading",
        "done": "done",
    }.get(book["status"], "queue")
    bar_len = 10
    pct = min(100, max(0, int((book["progress"] / book["pages"]) * 100))) if book["pages"] else 0
    filled = int(bar_len * pct / 100)
    bar = "#" * filled + "-" * (bar_len - filled)
    stars = colorize("★" * book["rating"], "star") + colorize("☆" * (5 - book["rating"]), "empty")
    print(f"  {colorize(book['title'], status)} — {book['pages']} pages [{bar}] {pct}%")
    print(f"    {stars} {colorize(book['status'].replace('_', ' ').title(), status)}")


def print_streak(days):
    if days > 0:
        print(colorize(f"🔥 {days} day streak!", "streak"))
    else:
        print(colorize("No streak yet. Start reading today!", "info"))
