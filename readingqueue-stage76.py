# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ReadingQueue
import sys


def main():
    try:
        ReadingQueue.run()
    except KeyboardInterrupt:
        print("\nStopped. See you next read!")
        sys.exit(0)


if __name__ == "__main__":
    main()
