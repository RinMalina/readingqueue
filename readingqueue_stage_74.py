# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ReadingQueue
def snapshot(a, b, keys=None):
    if keys is None:
        keys = sorted(set(list(a.keys()) + list(b.keys())))
    rows = []
    for key in keys:
        av = a.get(key)
        bv = b.get(key)
        if av == bv:
            rows.append("{:<30} {:<20}".format(key, ""))
        else:
            rows.append("{:<30} {:<20} -> {}".format(key, av, bv))
    return "\n".join(rows)


def compare_snapshots(before, after):
    if not isinstance(before, dict) or not isinstance(after, dict):
        raise TypeError("both states must be dictionaries")
    return snapshot(before, after)


def summarize_snapshot(before, after):
    diff = snapshot(before, after)
    changed = sum(1 for line in diff.splitlines() if line.rstrip().endswith("->"))
    return "{} field(s) changed:\n{}".format(changed, diff)
