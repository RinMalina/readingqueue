# === Stage 60: Add saved views for frequently used filters ===
# Project: ReadingQueue
SAVED_VIEWS = {
    "recently_finished": {"rating": None, "min_streak": 0, "progress": 1.0},
    "highly_rated": {"rating": 4, "min_streak": 0, "progress": None},
    "currently_reading": {"rating": None, "min_streak": 0, "progress": 0.0},
    "long_streaks": {"rating": None, "min_streak": 7, "progress": None},
}

def save_view(name, filters):
    SAVED_VIEWS[name] = dict(filters)

def load_view(name):
    return SAVED_VIEWS.get(name)

def list_views():
    return list(SAVED_VIEWS.keys())
