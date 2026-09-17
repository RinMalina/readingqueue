# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ReadingQueue
DEFAULT_SETTINGS = {
    "theme": "light",
    "default_shelf": "To Read",
    "streak_goal": 7,
    "auto_archive_days": 365,
    "show_progress_bar": True,
    "notification_enabled": True,
    "rating_scale": 5,
    "reading_unit": "pages",
    "reading_unit_default": 100,
    "sort_order": "date_added",
}


def get_settings():
    """Return the current settings dictionary."""
    if "settings" not in app_data:
        app_data["settings"] = dict(DEFAULT_SETTINGS)
    return app_data["settings"]


def update_settings(key, value):
    """Update a single setting by key, returning the new settings dict."""
    settings = get_settings()
    settings[key] = value
    app_data["settings"] = settings
    return settings


def reset_settings():
    """Reset all settings to defaults and return them."""
    return dict(DEFAULT_SETTINGS)
