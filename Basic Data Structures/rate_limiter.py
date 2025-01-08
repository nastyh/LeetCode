"""
Whenever you expose a web service / api endpoint, you need to implement a rate limiter to prevent abuse of the service (DOS attacks).

Implement a RateLimiter Class with an isAllow method. Every request comes in with a unique clientID,
deny a request if that client has made more than 100 requests in the past second.
"""

from collections import defaultdict
import time

class RateLimiter:
    """
    O(r), r num of requests in a one-sec period
    O(ur), u num of unique clients 
    Rate limiter to deny requests if a client exceeds 100 requests per second.
    """
    def __init__(self, max_requests_per_second=100):
        """
        Initializes the RateLimiter.

        :param max_requests_per_second: Maximum number of requests allowed per second.
        """
        self.max_requests_per_second = max_requests_per_second
        self.request_log = defaultdict(list)

    def is_allow(self, client_id):
        """
        Determines if a request is allowed for the given client ID.

        :param client_id: Unique identifier for the client.
        :return: True if the request is allowed, False otherwise.
        """
        current_time = time.time()
        request_times = self.request_log[client_id]

        # Remove requests that are outside the 1-second window
        while request_times and request_times[0] < current_time - 1:
            request_times.pop(0)

        if len(request_times) < self.max_requests_per_second:
            request_times.append(current_time)
            return True
        return False

# Example usage
if __name__ == "__main__":
    rate_limiter = RateLimiter()

    client_id = "client_1"

    # Simulate requests
    for i in range(105):
        if rate_limiter.is_allow(client_id):
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Blocked")
        time.sleep(0.01)  # Simulate rapid requests
