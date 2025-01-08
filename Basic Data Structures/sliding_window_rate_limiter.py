"""
implement API rate limiter
Implementation based on Sliding Window Algorithm that maintains the
map of requests at given timestamp and the counter for that (similar to Redis Hash)
"""
class SlidingWindowRateLimiter:
    """
    O(r), r max num of requests
    O(ur), u num of unique users 
    Rate limiter implementation using Sliding Window algorithm.
    """
    def __init__(self, max_requests, window_size):
        """
        :param max_requests: Maximum number of requests allowed in the time window
        :param window_size: Time window size in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.request_log = defaultdict(list)

    def is_allowed(self, user_id):
        """
        Checks if a request is allowed for the given user ID.

        :param user_id: Unique identifier for a user
        :return: True if the request is allowed, False otherwise
        """
        current_time = time.time()
        request_times = self.request_log[user_id]

        # Remove requests outside the sliding window
        while request_times and request_times[0] < current_time - self.window_size:
            request_times.pop(0)

        if len(request_times) < self.max_requests:
            request_times.append(current_time)
            return True
        return False

# Example usage for rate limiter
rate_limiter = SlidingWindowRateLimiter(max_requests=5, window_size=60)
user_id = "user_1"

for i in range(7):
    allowed = rate_limiter.is_allowed(user_id)
    print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
    time.sleep(10)  # Simulate time between requests