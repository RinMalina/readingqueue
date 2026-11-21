# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ReadingQueue
USAGE = """\
ReadingQueue - a simple, dependency-free reading tracker.

1) Install
   pip install -r requirements.txt

2) Run
   python main.py            # start the interactive console
   python --help             # list commands

3) Commands
   add <title> [--author] [--genre] [--pages]
       Add a book to your to-read queue.
   start <title>
       Begin reading a book.
   update <title> [--pages <n>] [--status <progress>]
       Log reading progress.
   finish <title> [--rating <1-5>] [--review]
       Complete a book and optionally rate it.
   list [--queue|--reading|--done|--all]
       Show your books by status.
   stats
       View reading stats and current streak.
   remove <title>
       Remove a book from the tracker.

4) Data
   Your data is stored in data/queue.json (created on first run).

5) Tips
   - Keep a daily update to grow your streak.
   - Rate books 1-5 to build your personal ratings.

6) Example session
   >>> add "The Hobbit" --pages 300
   >>> start "The Hobbit" --pages 150
   >>> update "The Hobbit" --pages 300
   >>> finish "The Hobbit" --rating 5
   >>> list --all
   >>> stats

Enjoy your reading journey!
"""
