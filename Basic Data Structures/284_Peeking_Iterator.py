from collections import deque
class PeekingIterator:  # O(N) both 
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.h = deque()
        while iterator.hasNext():
            self.h.appendleft(iterator.next())
        self.i = 0
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # print(self.i) #1
        return self.h[len(self.h)-(1)]
        
    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.h.pop()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.h) != 0


class PeekingIterator:  # O(n) and O(1)
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.to_peek

    def next(self):
        """
        :rtype: int
        """
        temp = self.to_peek
        self.to_peek = self.iterator.next() if self.iterator.hasNext() else None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.to_peek is not None