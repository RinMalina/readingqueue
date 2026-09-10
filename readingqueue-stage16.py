# === Stage 16: Add argparse support for the most common commands ===
# Project: ReadingQueue
import argparse

def main():
    parser = argparse.ArgumentParser(description="ReadingQueue CLI")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a book")
    p_add.add_argument("title")
    p_add.add_argument("--author", "-a")

    p_show = sub.add_parser("show", help="List books")
    p_show.add_argument("--by-status", "-s", choices=["all", "reading", "done", "to-read"], default="all")

    p_progress = sub.add_parser("progress", help="Show reading progress")
    p_progress.add_argument("--book", "-b")

    p_rate = sub.add_parser("rate", help="Rate a book")
    p_rate.add_argument("book")
    p_rate.add_argument("rating", type=int)

    p_streak = sub.add_parser("streak", help="Show reading streak")

    args = parser.parse_args()
    print(f"Command: {args.command}")
