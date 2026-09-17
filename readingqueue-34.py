# === Stage 34: Add support for multiple local user profiles ===
# Project: ReadingQueue
def load_profiles(profile_dir: str) -> dict[str, "ReadingProfile"]:
    profiles = {}
    for fname in os.listdir(profile_dir):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(profile_dir, fname), "r", encoding="utf-8") as fh:
            data = json.load(fh)
        profile = ReadingProfile(
            name=data["name"],
            books=json.loads(data["books"]),
            streaks=json.loads(data["streaks"]),
            stats=json.loads(data["stats"]),
        )
        profiles[profile.name] = profile
    return profiles
