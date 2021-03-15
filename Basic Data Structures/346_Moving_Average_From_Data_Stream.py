from collections import deque
class MovingAverage:  # optimal

    def __init__(self, size):  # O(1) and O(N) b/c it's only plus and minus. And the deque
        """
        Keep adding elements to nums that is a deque
        Also, keep track of the running sum in order not to recalculate sums
        Keep track of how many elements are in
        """
        self.size = size
        self.nums = deque()
        self.running = 0
        self.curr_length = 0

    def next(self, val):
        """
        Element comes in. Increment length, add to nums, add to running sum
        If after that we have more than size elements, we need to remove the oldest element
        both from nums, from running, and decrement curr_length
        Finally, return the result
        """
        self.curr_length += 1
        self.nums.append(val)
        self.running += val
        if self.curr_length > self.size:
            self.running -= self.nums.popleft()
            self.curr_length -= 1
        return self.running / self.curr_length



class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.window_sum = 0
        self.count = 0
        self.size = size

    def next(self, val):
        self.count += 1
        self.queue.append(val)
        popped = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - popped + val
        return self.window_sum / min(self.size, self.count)

