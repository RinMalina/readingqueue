# === Stage 46: Add a schema version field and migration helper ===
# Project: ReadingQueue
import json
import sqlite3
from pathlib import Path

SCHEMA_VERSION = 3
MIGRATION_FILE = Path(__file__).parent / "schema_migrations.json"


def get_current_schema_version(conn: sqlite3.Connection) -> int:
    """Return the recorded schema version from the metadata table."""
    try:
        cursor = conn.execute("SELECT version FROM schema_migrations WHERE version = ?", (SCHEMA_VERSION,))
        row = cursor.fetchone()
        return row[0] if row else 0
    except sqlite3.OperationalError:
        return 0


def bump_schema_version(conn: sqlite3.Connection) -> None:
    """Record the current schema version in the metadata table."""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS schema_migrations "
        "(version INTEGER PRIMARY KEY)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO schema_migrations (version) VALUES (?)",
        (SCHEMA_VERSION,),
    )
    conn.commit()


def run_migrations(conn: sqlite3.Connection) -> None:
    """Apply any pending migrations and log them to schema_migrations.json."""
    if MIGRATION_FILE.exists():
        with open(MIGRATION_FILE, "r") as f:
            migrations = json.load(f)
    else:
        migrations = []

    current = get_current_schema_version(conn)
    for m in migrations:
        if m["version"] <= current:
            continue
        conn.execute(m["sql"])
        conn.commit()
        migrations.append(m)
        current = m["version"]

    with open(MIGRATION_FILE, "w") as f:
        json.dump(migrations, f, indent=2)
