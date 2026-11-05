# === Stage 58: Add bulk update behavior for selected records ===
# Project: ReadingQueue
def bulk_update(self, records):
    """Update multiple records at once by their keys.

    Each entry in records is a dict with a 'key' field plus any fields
    to modify. Only provided fields are changed; missing fields keep
    their current values. Returns the number of records updated.
    """
    updated = 0
    for record in records:
        key = record.get('key')
        if key is None:
            continue
        if key in self.records:
            current = self.records[key]
            for field, value in record.items():
                if field != 'key':
                    current[field] = value
            self.last_modified = _now()
            updated += 1
    return updated


def bulk_set_status(self, status, keys):
    """Set a field for many records sharing the same key list.

    keys is an iterable of record keys to update. status is the value
    to assign to the given field. Returns the number of records set.
    """
    count = 0
    for key in keys:
        record = self.records.get(key)
        if record is not None:
            record[status] = status_value(status)
            self.last_modified = _now()
            count += 1
    return count
