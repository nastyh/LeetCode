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