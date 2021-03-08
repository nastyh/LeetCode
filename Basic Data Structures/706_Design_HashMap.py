class ListNode:
    def __init__(self, key, value):  # All times are O(N/K) where N is the number of all possible keys and K is the number of buckets (these are basically collisions)
        self.key = key
        self.value = value
        self.next = None

    def __init__(self):
            self.size = 1000
            self.hash_table = [None] * self.size 

    def put(self, key: int, value: int) -> None:
        index = key % self.size 
        if self.hash_table[index] == None:
            # We do not have anything in this bin, just create a new node 
            self.hash_table[index] = ListNode(key, value)
        else:
            # We do have something in this bin, traverse it checking to see if we have a matching key. If not just append a node to the end of the bin
            curr_node = self.hash_table[index]
            while True:
                if curr_node.key == key:
                    curr_node.value = value
                    return 
                if curr_node.next == None: break
                curr_node = curr_node.next 
            # Did not find a matching key here, so append a key, value pair in this bin
            curr_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size 
        curr_node = self.hash_table[index]
        while curr_node:
            if curr_node.key == key:
                return curr_node.value 
            else:
                curr_node = curr_node.next
        return -1
        
    def remove(self, key: int) -> None:
        index = key % self.size 
        
        curr_node = prev_node = self.hash_table[index]
        
        # Removing from empty bin just return
        if not curr_node: return 
        
        if curr_node.key == key:
            # We found the node to delete immediately, we can now skip over it 
            self.hash_table[index] = curr_node.next
        else:
            # We did not find the node to delete we must now traverse the bin
            curr_node = curr_node.next
            
            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next 
                    break
                else:
                    prev_node, curr_node = prev_node.next, curr_node.next


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap_bucket(object):  # O(N/K) and O(N + K) where N is the number of all possible keys and K is the number of predefiend buckets (by what youre dividing)
    """
    Take care of the design (just divide by the prime number as a hash function)
    and take care of the collisions 
    """
    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)