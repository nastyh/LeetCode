"""
Implement a rate limiter using a leaking bucket algorithm 
Modify it to be per user
Add a credit system for each user in case rate was not used 
"""

# JUST BASIC 

import time

class LeakingBucketRateLimiter:
    """
    O(1) both 
     Leaking Water: The _leak method calculates the amount of water (requests)
     leaked based on the elapsed time and the leak_rate. This ensures that requests are processed at a steady rate.

     Allowing Requests: The allow_request method first leaks the bucket,
     then checks if there’s room in the bucket for a new request. If there’s room, the request is allowed and the water level is incremented.

     Capacity and Leak Rate: The capacity determines the burst size (maximum number of requests that can be handled at once),
     while the leak_rate determines the steady rate at which requests are processed.


    """
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize the rate limiter with a bucket capacity and leak rate.
        
        :param capacity: Maximum number of requests the bucket can hold.
        :param leak_rate: Number of requests leaked per second.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_water_level = 0  # Current requests in the bucket
        self.last_checked = time.time()  # Last time the bucket was updated

    def _leak(self):
        """
        Update the water level in the bucket by leaking water (requests) since the last check.
        """
        now = time.time()
        elapsed_time = now - self.last_checked
        leaked = elapsed_time * self.leak_rate
        self.current_water_level = max(0, self.current_water_level - leaked)
        self.last_checked = now

    def allow_request(self) -> bool:
        """
        Check if a request can be allowed and update the bucket.
        
        :return: True if the request is allowed, False otherwise.
        """
        self._leak()  # Leak the bucket before checking

        if self.current_water_level < self.capacity:
            # There is room in the bucket; accept the request
            self.current_water_level += 1
            return True
        else:
            # Bucket is full; reject the request
            return False


# MODIFY IT TO BE PER USER
import time

class LeakingBucket:
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize a bucket with a capacity and leak rate.
        
        :param capacity: Maximum number of requests the bucket can hold.
        :param leak_rate: Number of requests leaked per second.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_water_level = 0
        self.last_checked = time.time()

    def _leak(self):
        """
        Leak water (requests) from the bucket based on the elapsed time.
        """
        now = time.time()
        elapsed_time = now - self.last_checked
        leaked = elapsed_time * self.leak_rate
        self.current_water_level = max(0, self.current_water_level - leaked)
        self.last_checked = now

    def allow_request(self) -> bool:
        """
        Check if the request can be allowed based on the current bucket state.
        
        :return: True if the request is allowed, False otherwise.
        """
        self._leak()  # Leak the bucket before checking

        if self.current_water_level < self.capacity:
            # There is room in the bucket; accept the request
            self.current_water_level += 1
            return True
        else:
            # Bucket is full; reject the request
            return False


class PerUserRateLimiter:
    """
    O(1)
    O(u), unique users making requests. Each user has their own bucket
    To be user-specific, we can maintain a separate bucket for each user.
    This can be achieved using a dictionary where the key is the user ID and the value is a bucket object.
    """
    def __init__(self, capacity: int, leak_rate: float):
        """
        Initialize the per-user rate limiter with shared capacity and leak rate.
        
        :param capacity: Maximum number of requests a user's bucket can hold.
        :param leak_rate: Number of requests leaked per second for each user's bucket.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.user_buckets = {}

    def allow_request(self, user_id: str) -> bool:
        """
        Check if a request from a specific user can be allowed.
        
        :param user_id: The unique ID of the user making the request.
        :return: True if the request is allowed, False otherwise.
        """
        if user_id not in self.user_buckets:
            # Create a new bucket for the user if it doesn't exist
            self.user_buckets[user_id] = LeakingBucket(self.capacity, self.leak_rate)

        # Check the user's bucket for allowance
        return self.user_buckets[user_id].allow_request()

# CREDIT SYSTEM FOR USERS

import time

class LeakingBucketWithCredits:
    """
    O(1)
    O(u), unique users making requests 
    Credit System:

    Unused capacity is tracked as credits in the _leak method.
    Credits are accumulated at the same rate as the bucket leaks (based on elapsed_time and unused capacity).
    Using Credits:

    If the bucket is full, the limiter checks if the user has available credits.
    If credits exist, they are used to allow the request, reducing the credit balance.
    Maximum Credits:

    The max_credits parameter limits how much unused capacity can be accumulated over time.
    Independent Per-User State:

    Each user has their own bucket with separate water levels, credits, and timestamps.
    """
    def __init__(self, capacity: int, leak_rate: float, max_credits: int):
        """
        Initialize a bucket with capacity, leak rate, and maximum credit storage.
        
        :param capacity: Maximum number of requests the bucket can hold at any moment.
        :param leak_rate: Number of requests leaked per second.
        :param max_credits: Maximum unused credits a user can accumulate.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_water_level = 0
        self.credits = 0
        self.max_credits = max_credits
        self.last_checked = time.time()

    def _leak(self):
        """
        Leak water (requests) from the bucket based on the elapsed time.
        """
        now = time.time()
        elapsed_time = now - self.last_checked
        leaked = elapsed_time * self.leak_rate
        self.current_water_level = max(0, self.current_water_level - leaked)
        
        # Accumulate credits for unused capacity
        unused_capacity = max(0, self.capacity - self.current_water_level)
        self.credits = min(self.credits + unused_capacity * elapsed_time, self.max_credits)
        
        self.last_checked = now

    def allow_request(self) -> bool:
        """
        Check if the request can be allowed based on the current bucket state.
        
        :return: True if the request is allowed, False otherwise.
        """
        self._leak()  # Leak the bucket before checking

        if self.current_water_level < self.capacity:
            # There is room in the bucket; accept the request
            self.current_water_level += 1
            return True
        elif self.credits > 0:
            # Use credits if available
            self.credits -= 1
            return True
        else:
            # Bucket is full and no credits left; reject the request
            return False


class PerUserRateLimiterWithCredits:
    """
    allow users to accumulate unused capacity (credits) if they don’t use their rate limit fully.
    This means if a user doesn't send requests for a while, they "save" credits, which they can use
    later to exceed the normal rate limit for short bursts.
    """
    def __init__(self, capacity: int, leak_rate: float, max_credits: int):
        """
        Initialize the per-user rate limiter with shared capacity, leak rate, and credit system.
        
        :param capacity: Maximum number of requests a user's bucket can hold at any moment.
        :param leak_rate: Number of requests leaked per second for each user's bucket.
        :param max_credits: Maximum credits a user can accumulate.
        """
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.max_credits = max_credits
        self.user_buckets = {}

    def allow_request(self, user_id: str) -> bool:
        """
        Check if a request from a specific user can be allowed.
        
        :param user_id: The unique ID of the user making the request.
        :return: True if the request is allowed, False otherwise.
        """
        if user_id not in self.user_buckets:
            # Create a new bucket for the user if it doesn't exist
            self.user_buckets[user_id] = LeakingBucketWithCredits(
                self.capacity, self.leak_rate, self.max_credits
            )

        # Check the user's bucket for allowance
        return self.user_buckets[user_id].allow_request()
