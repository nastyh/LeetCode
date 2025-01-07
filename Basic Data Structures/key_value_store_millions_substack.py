"""
First is just a basic implementation
Then optimized for millions of values and repeating values 
"""
class KeyValueStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        """Set the value for a given key."""
        self.store[key] = value

    def get(self, key):
        """Retrieve the value for a given key."""
        return self.store.get(key, None)

    def delete(self, key):
        """Delete a key from the store."""
        if key in self.store:
            del self.store[key]

    def exists(self, key):
        """Check if a key exists in the store."""
        return key in self.store

    def keys(self):
        """Return all keys in the store."""
        return list(self.store.keys())

    def values(self):
        """Return all values in the store."""
        return list(self.store.values())

    def clear(self):
        """Clear the entire store."""
        self.store.clear()

"""
LARGE SCALE
Storing a million keys and potentially repeating values can consume significant memory.
Retrieval, insertion, and deletion need to remain efficient, ideally O(1)
Avoid storing duplicate values redundantly
combination of hash maps and deduplication:
Store values in a separate pool (like a list or dictionary).
Keys point to the index or reference in the value pool.

Further Optimizations
Use databases like SQLite or key-value stores like Redis for external storage when memory becomes a bottleneck.
Compress values in the value_pool to further reduce memory usage.
Support batch inserts and queries for large-scale workloads.
"""

class OptimizedKeyValueStore:
    def __init__(self):
        self.key_to_index = {}  # Maps keys to indices in value pool
        self.value_pool = {}    # Maps hash of value to actual value

    def set(self, key, value):
        """Set the value for a given key with deduplication."""
        value_hash = hash(value)
        if value_hash not in self.value_pool:
            self.value_pool[value_hash] = value
        self.key_to_index[key] = value_hash

    def get(self, key):
        """Retrieve the value for a given key."""
        value_hash = self.key_to_index.get(key)
        if value_hash is None:
            return None
        return self.value_pool[value_hash]

    def delete(self, key):
        """Delete a key from the store."""
        if key in self.key_to_index:
            del self.key_to_index[key]

    def exists(self, key):
        """Check if a key exists in the store."""
        return key in self.key_to_index

    def keys(self):
        """Return all keys in the store."""
        return list(self.key_to_index.keys())

    def values(self):
        """Return all unique values in the store."""
        return list(self.value_pool.values())

    def clear(self):
        """Clear the entire store."""
        self.key_to_index.clear()
        self.value_pool.clear()
