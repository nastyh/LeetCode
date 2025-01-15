"""
Implement a system to track the popularity of content based on user interactions (thumbs up or thumbs down).
Your task is to design an interface called ContentPopularity with the following methods:

1. increasePopularity(contentId: int) -> None: Increases the popularity of the specified content ID by one (representing a thumbs up).

2. decreasePopularity(contentId: int) -> None: Decreases the popularity of the specified content ID by one (representing a thumbs down). 

3. mostPopular() -> int: Returns the content ID with the highest popularity. If there are ties, return any one of them. -1 if no content.
"""

from collections import defaultdict
import heapq

class ContentPopularity:
    """
    O(nlogn)
    O(N)
    just have a dict: id: units of popularity
    and max heap to access the most popular id. 
    Since it's a min heap by default, add -unit of popularity to have the most
    popular on top
    """
    def __init__(self):
        # Dictionary to track the popularity of each content
        self.popularity = defaultdict(int)
        # Min-heap to efficiently track the most popular content
        # Stores tuples in the form (-popularity, contentId) for max-heap behavior
        self.heap = []

    def increasePopularity(self, contentId: int) -> None:
        self.popularity[contentId] += 1
        # Push updated popularity into the heap
        heapq.heappush(self.heap, (-self.popularity[contentId], contentId))

    def decreasePopularity(self, contentId: int) -> None:
        if contentId in self.popularity:
            self.popularity[contentId] -= 1
            # Push updated popularity into the heap
            heapq.heappush(self.heap, (-self.popularity[contentId], contentId))

    def mostPopular(self) -> int:
        while self.heap:
            # Get the most popular content (max heap, so negative value is used)
            current_popularity, contentId = heapq.heappop(self.heap)
            if -current_popularity == self.popularity[contentId]:
                # If the heap's popularity matches the current popularity, return it
                return contentId

        return -1  # No content available

# Example usage:
cp = ContentPopularity()
cp.increasePopularity(1)
cp.increasePopularity(2)
cp.increasePopularity(1)
cp.decreasePopularity(2)
print(cp.mostPopular())  # Should print 1
