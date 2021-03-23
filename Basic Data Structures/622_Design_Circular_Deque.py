class MyCircularDeque:  # O(1) except the __init__ portion 
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = k
        self.arr  = [None] * k  # O(n) initialization
        # self.arr = {} #  O(1) initialization (completes full O(1) code)
        self.head = self.tail = None
        self.busy = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.head is None:
            self.head = self.tail = 0
        else:
            new = (self.head+1)%self.size
            if new == self.tail:
                return False
            self.head = new
        self.arr[self.head] = value
        self.busy += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.tail is None:
            self.head = self.tail = 0
        else:
            new = (self.tail-1)%self.size
            if new == self.head:
                return False
            self.tail = new
        self.arr[self.tail] = value
        self.busy += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.head is None:
            return False
        self.arr[self.head] = None
        self.busy -= 1
        if self.tail == self.head:
            self.head = self.tail = None
        else:
            self.head = (self.head - 1) % self.size
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.tail is None:
            return False
        self.arr[self.tail] = None
        self.busy -= 1
        if self.tail==self.head:
            self.head = self.tail = None
        else:
            self.tail = (self.tail + 1) % self.size
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.head is None:
            return -1
        return self.arr[self.head]
    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.tail is None:
            return -1
        return self.arr[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.head is None

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.busy == self.size