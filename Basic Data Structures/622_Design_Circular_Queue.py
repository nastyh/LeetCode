class MyCircularQueue_short:  # O(1) for everything except init. O(N)
    """
    Given a fixed size array, any of the elements could be considered as a head in a queue.
    tail_ix = (head_ix + count - 1) % capacity
    """
    def __init__(self, k: int):
        self.q = [None] * k  # queue itself
        self.size = k  # so that we don't call len(self.q) all the time 
        self.taken = 0  # how many values are inserted so far
        self.front = -1 # insertion index. Start with -1, so that after inserting the first value we're at index 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.front = (self.front + 1) % self.size
        self.q[self.front] = value
        self.taken += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.taken -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.q[(self.front - self.taken + 1) % self.size]  # this is the key of the question here 

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.q[self.front]  # value at an index at which we inserted the value 
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.taken == 0  # if we haven't taken anyting, it should be 0
        
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.taken == self.size  # if we took every possible empty slot



class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.k = k
        self.front = self.rear = -1
        self.cur_size = 0
        

    def enQueue(self, value: int):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front + 1) % self.k
        self.q[self.front] = value
        self.cur_size += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = None
        self.cur_size -= 1
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        idx = (self.rear + 1) % self.k
        return self.q[idx]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cur_size == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.cur_size == self.k


class MyCircularQueue_another:

    def __init__(self, k: int):
        self.data = [None] * k
        self.head = self.tail = self.num_entries = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % len(self.data)
        self.num_entries += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.num_entries -= 1
        self.head = (self.head + 1) % len(self.data)
        return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head] 

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.tail - 1) % len(self.data)]
        
    def isEmpty(self) -> bool:
        return self.num_entries == 0
        
    def isFull(self) -> bool:
        return self.num_entries == len(self.data)