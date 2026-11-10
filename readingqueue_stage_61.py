# === Stage 61: Add performance timing for core list and search operations ===
# Project: ReadingQueue
import time


def _now():
    return time.perf_counter()


class _TimedList:
    def __init__(self, data=None):
        self._data = list(data or [])
        self._hits = {}
        self._calls = 0
        self._max_ms = 0.0

    def append(self, item):
        self._data.append(item)
        return self

    def insert(self, index, item):
        self._data.insert(index, item)
        return self

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def clear(self):
        self._data.clear()
        self._hits.clear()

    def _time(self, func):
        def wrapper(*args, **kwargs):
            self._calls += 1
            start = _now()
            result = func(*args, **kwargs)
            elapsed = (_now() - start) * 1000.0
            if elapsed > self._max_ms:
                self._max_ms = elapsed
            return result
        return wrapper

    def search(self, predicate):
        self.search = self._time(self.search)
        return self.search(predicate)

    def search_index(self, predicate):
        self.search_index = self._time(self.search_index)
        for i, item in enumerate(self._data):
            if predicate(item):
                return i
        return -1

    def all(self, predicate):
        self.all = self._time(self.all)
        return [item for item in self._data if predicate(item)]

    def count(self, predicate=None):
        self.count = self._time(self.count)
        if predicate is None:
            return len(self._data)
        return sum(1 for item in self._data if predicate(item))

    def stats(self):
        return {
            "operations": self._calls,
            "max_search_ms": round(self._max_ms, 3),
            "size": len(self._data),
        }
