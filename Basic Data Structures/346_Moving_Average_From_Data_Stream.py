from collections import deque
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

