# === Stage 53: Add command help text and usage examples ===
# Project: ReadingQueue
def print_help():
    usage = (
        "Usage: python readingqueue.py <command> [options]"
    )
    print(usage)
    print()
    print("Commands:")
    print("  add <title> [author]    Add a book to your to-read queue")
    print("  start <title>           Begin reading a book")
    print("  progress <title>        Show current reading progress")
    print("  rate <title> <stars>    Rate a finished book (1-5 stars)")
    print("  streak                  Show your current reading streak")
    print("  list                    List your to-read queue")
    print("  help                    Show this help message")
    print()
    print("Examples:")
    print("  python readingqueue.py add 'The Hobbit' 'Tolkien'")
    print("  python readingqueue.py start 'The Hobbit'")
    print("  python readingqueue.py progress 'The Hobbit'")
    print("  python readingqueue.py rate 'The Hobbit' 5")
    print("  python readingqueue.py streak")
    print("  python readingqueue.py help")
