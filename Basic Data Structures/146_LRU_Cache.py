from collections import OrderedDict
"""
Time complexity: O(1)O(1)O(1) for both get and put.
Space: O(capacity)
For our LRUCache class, we need the following attributes:

capacity - to detect when we need to start deleting key-value pairs.
dic - short for dictionary, this will be our hash map that maps keys to nodes.
head - the head of our linked list
tail - the tail of our linked list

The cleanest way to handle the empty list case is by using sentinel nodes.
We will have our head and tail attributes both set to dummy nodes. 
The "real" head will be head.next and the "real" tail will be tail.prev. These dummy nodes sit just "outside" of our linked list. What is the purpose? We never want head or tail to be null.
"""

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Now that we have helper methods for adding and removing from our linked list, we can easily implement the get and put methods using simple logic.
        Check if key exists in the hash map. If not, return -1.
        Get the node associated with key from the hash map.
        Move it to the back of the linked list. This can be done by first calling remove(node) and then add(node).
        Return the value associated with key, which is node.val.
        """
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        This method updates key: value if it already exists, and inserts key: value otherwise. If inserting causes the size to exceed capacity, we need to remove the least recently used key (which we know is the head of our linked list).
        We can perform the following steps:
        First, check if key already exists in the hash map. If it does, find the node associated with it and call remove on it.
        We are going to move the key to the back of the queue, so we need to first remove it from the linked list.
        Create a new node using key, value.
        Set key: node in the hash map.
        Add node to the back of the linked list with add(node).
        Finally, check if the data structure has exceeded capacity by using the hash map's size.
        If it has, then get the nodeToDelete as head.next.
        Delete the node with remove(nodeToDelete).
        Delete the key from the hash map. The key is nodeToDelete.key.
        """
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        """
        We need to add a node to the end of our linked list whenever we add a new key or update an existing one.
        """
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """
        We need to perform removals when we update/fetch an existing key,
        or when the data structure exceeds capacity
        """
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

########################################
class LRUCache:

    def __init__(self, capacity: int):
        self.storage = OrderedDict()
        self.capacity = capacity
        # self.space_left = self.capacity - len(self.storage)
        

    def get(self, key: int) -> int:
        if key in self.storage.keys():
            val = self.storage[key]
            self.storage.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage: del self.storage[key]
        self.storage[key] = value
        if len(self.storage) > self.capacity:
            self.storage.popitem(last=False)

# creating a doubly linked list from scratch

    class Node:
    
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.pre = None

class Dll:
    
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0
    
    def removeNode(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre

    def addNode(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
          
    def update(self, node):
        self.removeNode(node)
        self.addNode(node)
        
    def insert(self, node):
        self.addNode(node)
        self.count += 1
        return node
    
    def removeLast(self):
        last = self.tail.pre
        self.removeNode(last)
        self.count -= 1
        return last
        
class LRUCache:

    def __init__(self, capacity):
        self.dll = Dll()
        self.dic = {}
        self.cap = capacity

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.dll.update(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.dll.update(node)
        else:
            if self.dll.count == self.cap:
                last = self.dll.removeLast()
                del self.dic[last.key]
            node = Node(key, value)
            self.dic[key] = node
            self.dll.insert(node)
