# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ReadingQueue
if __name__ == "__main__":
    import os

    def validate():
        if not os.path.isfile(READINGS_FILE):
            raise FileNotFoundError("Readings file missing")
        if not os.path.isfile(SHARED_FILE):
            raise FileNotFoundError("Shared state file missing")

    def demo():
        rq = ReadingQueue()
        rq.add_book("Dune", "Friedman")
        rq.add_book("1984", "Orwell")
        rq.start_book("Dune")
        rq.mark_page("Dune", 120)
        rq.rate_book("Dune", 5)
        rq.finish_book("Dune")
        rq.complete_page("1984", 250)
        print("Queue:", len(rq.queue))
        print("Progress:", rq.progress)
        print("Streak:", rq.streak)
        print("Rating:", rq.rating("Dune"))

    validate()
    demo()
