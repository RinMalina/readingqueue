# === Stage 19: Add undo support for the last simple mutation ===
# Project: ReadingQueue
def undo_last(self):
    if not self.history:
        return
    state, op = self.history.pop()
    if op == "add":
        self.queue.remove(state)
    elif op == "remove":
        self.queue.append(state)
    elif op == "update_progress":
        self.queue.append(state)
    elif op == "rate":
        self.queue.append(state)
    elif op == "update_streak":
        self.queue.append(state)
