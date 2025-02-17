import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        O(nlogn)
        O(n)
        Sort the events by start day
        Use a min-heap to track the end days of ongoing events
        iterate through days, add events that start on that day.
        Remove events that have already ended (i.e., their end day is less than the current day).
        Attend the event that ends the earliest.
        Continue until all days and events are processed.
        """
        events.sort(key = lambda x: x[0])
        res = 0
        h = []
        i = 0
        curr_day = 0 if len(events) == 0 else events[0][0]
        while i < len(events) or h:
            while i < len(events) and events[i][0] <= curr_day:
                heapq.heappush(h, events[i][1])
                i += 1
            while h and h[0] < curr_day:
                heapq.heappop(h)
            if h:
                heapq.heappop(h)
                res += 1
                curr_day += 1
            else:
                # If no event is available to attend, jump to the next event's start day.
                if i < len(events):
                    curr_day = events[i][0]
        return res