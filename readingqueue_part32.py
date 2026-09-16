# === Stage 32: Add pagination helpers for long console output ===
# Project: ReadingQueue
def paginate(lines, chunk=10):
    for i in range(0, len(lines), chunk):
        end = min(i + chunk, len(lines))
        print(''.join(lines[i:end]))
        if i + chunk < len(lines):
            print()  # blank line between chunks
