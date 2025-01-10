import math
class AllOne:

    def __init__(self):
        self.d = {} # key: count
        self.count_keys_d = {} # counts: set of keys
        self.max_key_value = -math.inf # actually it means the max count for a given key
        self.min_key_value = math.inf # actually it means the min count for a given key

    def inc(self, key: str) -> None:
        """
        Increments the count of key by 1. If the key is new, it initializes its count to 1.
        """
        if key in self.d:
            count = self.d[key]
            self.count_keys_d[count].remove(key)
            if not self.count_keys_d[count]:
                del self.count_keys_d[count]
                if self.min_key_value == count:
                    self.min_key_value += 1
            count += 1
        else:
            count = 1
            self.min_key_value = min(self.min_key_value, count)
        self.d[key] = count 
        if count not in self.count_keys_d:
            self.count_keys_d[count] = set()
        self.count_keys_d[count].add(key)
        self.max_key_value = max(self.max_key_value, count)

    def dec(self, key: str) -> None:
        """
        Decrements the count of key by 1. Removes the key if its count reaches 0.
        """
        count = self.d[key]
        self.count_keys_d[count].remove(key)
        if not self.count_keys_d[count]:
            del self.count_keys_d[count]
            if self.max_key_value == count:
                self.max_key_value -= 1

        if count == 1:
            del self.d[key]
            if not self.max_key_value:
                self.min_key_value = float('inf')
                self.max_key_value = float('-inf')
            else:
                self.min_key_value = min(self.count_keys_d.keys())
        else:
            count -= 1
            self.d[key] = count
            if count not in self.count_keys_d:
                # set is good since adding/removing is O(1)
                self.count_keys_d[count] = set()
            self.count_keys_d[count].add(key)
            self.min_key_value = min(self.min_key_value, count)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with the maximum count, or an empty string if no keys exist.
        """
        if self.max_key_value == float('-inf'):
            return ""
        return next(iter(self.count_keys_d[self.max_key_value]))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with the minimum count, or an empty string if no keys exist.
        """
        if self.min_key_value == float('inf'):
            return ""
        return next(iter(self.count_keys_d[self.min_key_value]))