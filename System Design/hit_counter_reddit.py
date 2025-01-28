"""
Write a hit counter that fits the following interface:
public interface HitCounter {
  // Registers a hit at the timestamp.
  public void hit(int timestamp);
  // Returns the number of hits within 5 minutes of the timestamp.
  public int getHits(int timestamp);
}
getHits is always going to be called with a timestamp at least as large as the largest
timestamp you've seen so far. For this reason, a queue would be extremely inefficient.
The hits might come out of order. For example:
HitCounter hitCouner = new HitCounter();
hitCounter.hit(10);
hitCounter.hit(9);
hitCounter. getHits(100); // returns 2
hitCounter.hit(201);
hitCounter.hit(1);
hitCounter. getHits(400); // returns 2 (100 and 201)
Test it.
Follow up: Make it threadsafe.
"""

# WITHOUT threadsafe, first question

class HitCounter:
    def __init__(self):
        # Dictionary to store hits per timestamp
        self.hits = {}

    def hit(self, timestamp):
        """
        Registers a hit at the given timestamp.
        Time Complexity: O(1)
        Space Complexity: O(n), where n is the number of unique timestamps.
        """
        if timestamp in self.hits:
            self.hits[timestamp] += 1
        else:
            self.hits[timestamp] = 1

    def getHits(self, timestamp):
        """
        Returns the number of hits within the last 5 minutes (300 seconds).
        
        Time Complexity: O(n), where n is the number of unique timestamps in the hits dictionary.
        Space Complexity: O(n), where n is the number of unique timestamps.
        """
        start_time = timestamp - 300
        total_hits = 0

        # Count hits within the 5-minute window
        for time, count in list(self.hits.items()):
            if time > start_time:
                total_hits += count
            else:
                # Remove old timestamps
                del self.hits[time]

        return total_hits

# Testing the HitCounter
if __name__ == "__main__":
    hitCounter = HitCounter()

    # Test case 1: Hits out of order
    hitCounter.hit(10)
    hitCounter.hit(9)
    print(hitCounter.getHits(100))  # Expected: 2

    # Test case 2: Hits over a larger range
    hitCounter.hit(201)
    hitCounter.hit(1)
    print(hitCounter.getHits(400))  # Expected: 2 (100 and 201)


# FOLLOW-UP

from threading import Lock

class HitCounter:
    def __init__(self):
        # Dictionary to store hits per timestamp
        self.hits = {}
        self.lock = Lock()  # Lock for thread safety

    def hit(self, timestamp):
        """
        Registers a hit at the given timestamp.
        
        Time Complexity: O(1)
        Space Complexity: O(n), where n is the number of unique timestamps.
        """
        with self.lock:
            if timestamp in self.hits:
                self.hits[timestamp] += 1
            else:
                self.hits[timestamp] = 1

    def getHits(self, timestamp):
        """
        Returns the number of hits within the last 5 minutes (300 seconds).
        
        Time Complexity: O(n), where n is the number of unique timestamps in the hits dictionary.
        Space Complexity: O(n), where n is the number of unique timestamps.
        """
        with self.lock:
            start_time = timestamp - 300
            total_hits = 0

            # Count hits within the 5-minute window
            for time, count in list(self.hits.items()):
                if time > start_time:
                    total_hits += count
                else:
                    # Remove old timestamps
                    del self.hits[time]

            return total_hits

# Testing the HitCounter
if __name__ == "__main__":
    hitCounter = HitCounter()

    # Test case 1: Hits out of order
    hitCounter.hit(10)
    hitCounter.hit(9)
    print(hitCounter.getHits(100))  # Expected: 2

    # Test case 2: Hits over a larger range
    hitCounter.hit(201)
    hitCounter.hit(1)
    print(hitCounter.getHits(400))  # Expected: 2 (100 and 201)

# Follow-up: Thread safety
# The use of threading.Lock ensures that operations on the hits dictionary are thread-safe.
