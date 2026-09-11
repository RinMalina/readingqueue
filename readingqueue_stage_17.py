# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ReadingQueue
import argparse

def dry_run_mode(argv=None):
    """Set dry-run mode in a single global flag, usable by any command."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", default=False)
    return parser.parse_args(argv)
