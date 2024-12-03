class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.intervals:
            # No overlap condition:
            # incoming end <= existing start or incoming_start >= existing end 
            if not (endTime <= s or startTime >=e):
                return False 
        self.intervals.append((startTime, endTime))
        return True

# binary search

class MyCalendar:

    def __init__(self):
        self.L = []
        self.m = {}

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_right(self.L, startTime)
        if idx == len(self.L) or self.m[self.L[idx]] >= endTime:
            bisect.insort(self.L, endTime)
            self.m[endTime] = startTime
            return True

        return False