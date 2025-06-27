"""
# Historical Traversal Speeds

#Q:

# We have a graph of road segments, where each road segment has a string
# identifier. As the self driving car crosses the length of one of
# these segments, we measure the speed at which it traversed the segment.
# We're building a service to track road speeds. Implement two functions,
# one to receive reports of the speed from self-driving cars on the road and
# one that can return the average speed of that road segment over the
# last day.
# Assume this is a long lived service running for months or years.


# CODE

# Implement a class that has two methods:
#    report_speed
#          takes a segment_id and a speed
#    get_avg_speed_last_day
#             takes a segment id
#             returns the average speed for the last 24 hours'
"""
from collections import defaultdict, deque
from time import time

class RoadSpeedTracker:
    def __init__(self):
        self.segment_data = defaultdict(deque)  # segment_id -> deque of (timestamp, speed)
        self.DAY_SECONDS = 86400  # 24 hours in seconds

    def report_speed(self, segment_id: str, speed: float) -> None:
        now = time()
        self.segment_data[segment_id].append((now, speed))

    def get_avg_speed_last_day(self, segment_id: str) -> float:
        now = time()
        dq = self.segment_data[segment_id]
        
        # Evict old entries
        while dq and dq[0][0] < now - self.DAY_SECONDS:
            dq.popleft()
        
        if not dq:
            return 0.0  # or None, if preferred

        total_speed = sum(speed for _, speed in dq)
        return total_speed / len(dq)


# MOVING EVICTION TO report_speed()

from collections import defaultdict, deque
from time import time

class RoadSpeedTracker:
    def __init__(self):
        self.segment_data = defaultdict(deque)
        self.DAY_SECONDS = 86400  # 24 hours

    def report_speed(self, segment_id: str, speed: float) -> None:
        now = time()
        dq = self.segment_data[segment_id]
        dq.append((now, speed))
        
        # 🚫 Clean up stale data *during reporting*
        while dq and dq[0][0] < now - self.DAY_SECONDS:
            dq.popleft()

    def get_avg_speed_last_day(self, segment_id: str) -> float:
        dq = self.segment_data[segment_id]
        if not dq:
            return 0.0
        total_speed = sum(speed for _, speed in dq)
        return total_speed / len(dq)


# IF MANY CALLS TO report_speed() many cars on the same segments

from collections import defaultdict, deque
from time import time

class RoadSpeedTracker:
    def __init__(self):
        self.DAY_SECONDS = 86400
        self.segment_data = defaultdict(lambda: {
            "deque": deque(),           # (timestamp, speed)
            "total_speed": 0.0,         # running sum of valid speeds
            "count": 0                  # number of valid entries
        })

    def report_speed(self, segment_id: str, speed: float) -> None:
        now = time()
        data = self.segment_data[segment_id]
        dq = data["deque"]
        
        dq.append((now, speed))
        data["total_speed"] += speed
        data["count"] += 1

        # 🚫 Remove old entries
        while dq and dq[0][0] < now - self.DAY_SECONDS:
            old_time, old_speed = dq.popleft()
            data["total_speed"] -= old_speed
            data["count"] -= 1

    def get_avg_speed_last_day(self, segment_id: str) -> float:
        data = self.segment_data[segment_id]
        if data["count"] == 0:
            return 0.0
        return data["total_speed"] / data["count"]
