from collections import defaultdict, OrderedDict
"""
All operations (get and put) must run in O(1) time complexity.
Key to Value Mapping: Use a dictionary to store the key-value pairs for O(1) access
Key to Frequency Mapping: Use a dictionary to track the frequency of each key.
Frequency Groups: Use another dictionary where keys are frequencies, and values are ordered dictionaries (to maintain LRU order).
"""

class LFUCache:
    """
    O(1) for get and put
    O(n), n is cache capacity
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}       # Map key to value
        self.key_to_freq = {}      # Map key to frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # Map frequency to keys in LRU order
        self.min_freq = 0          # Track the minimum frequency in the cache
    
    def _update_frequency(self, key):
        """Helper function to update the frequency of a key."""
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq].pop(key)  # Remove the key from the current frequency group
        # If the current frequency group is empty and it was the minimum frequency, update min_freq
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        # Increment the frequency and add the key to the new frequency group
        self.key_to_freq[key] += 1
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq][key] = None  # Add the key to the new frequency group
    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        # Update the frequency of the key
        self._update_frequency(key)
        return self.key_to_val[key]
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val:
            # Update the value and frequency
            self.key_to_val[key] = value
            self._update_frequency(key)
        else:
            # Evict the least frequently used item if at capacity
            if len(self.key_to_val) >= self.capacity:
                # Evict the least frequently used and least recently used key
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val[evict_key]
                del self.key_to_freq[evict_key]
            
            # Add the new key-value pair
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1  # Reset the min frequency to 1 for the new key


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)