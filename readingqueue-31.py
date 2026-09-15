# === Stage 31: Add compact table rendering for long lists ===
# Project: ReadingQueue
def render_compact_table(headers, rows):
    """Render a compact table suitable for long lists."""
    if not rows:
        return "No data."
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    lines = [
        "┌" + "┬".join("─" * w for w in col_widths) + "┐",
    ]
    lines.append("│" + "│".join(str(h).center(w) for h, w in zip(headers, col_widths)) + "│")
    lines.append("├" + "┼".join("─" * w for w in col_widths) + "┤")
    for row in rows:
        lines.append("│" + "│".join(str(c).ljust(w) for c, w in zip(row, col_widths)) + "│")
    lines.append("└" + "┴".join("─" * w for w in col_widths) + "┘")
    return "\n".join(lines)
