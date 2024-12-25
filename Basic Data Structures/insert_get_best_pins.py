"""
Implement a class
def insert_data(self, pin_id, ts, pin_score)
pin with an id, with ts, with a score come to a DB
ts is always increasing

def get_best_pin(self, curr_time, window)
return a pin with a max score from a window [curr_time - window; curr_time]
can't throw away the old data 

Example:
xyz = user()
data = [("A", 0, 10), ("B", 1, 40), ("C", 2, 30), ("D", 7, 5)]
for pin, time, score in data:
	xyz.insert_data(pin, time, score)

print(xyz.get_best_pin(current_time = 7, window = 5)) # you should get C
print(xyz.get_best_pin(current_time = 7, window = 1)) # you should get D
print(xyz.get_best_pin(current_time = 7, window = 7)) # you should get B
"""
Class Pins:
    def __init__(self):
        self.d = deque() # stores (time, pin_id, score)
    
    def insert_data(self, pin: str, time: int, score: int): 
        """
        O(1) to insert and for space 
        """
        self.d.append((time, pin, score))
    
    def get_best_pin(self, curr_time: int, window: int) -> str:
        # Returns the pin with the maximum score within the given window.
        # O(n) time and O(1) space 
        res = None
        best_score = -1
        for time, pin, score in self.d: 
            if time >= curr_time - window: # whether a given data point within a window of interest 
                if score > best_score:
                    best_score = score 
                    res = pin 
        return res 


# USING A HEAP

Class Pins_heap:
    def __init__(self):
        self.data = []  # Store (time, pin, score) tuples
    
    def insert_data(self, pin: str, time: int, score: int): 
        """
        O(nlogn)
        """
        self.data.append((-score, time, pin)) # to have cheap access to the largest score 
    
    def get_best_pin(self, curr_time: int, window: int) -> str:
        # O(nlogn) both 
        heapq.heapify(self.data)
        best_pin = None
        best_score = -float('inf') 

        while self.data and self.data[0][1] < current_time - window:
            # remove data older that a window
            heapq.heappop(self.data)

        while self.data and self.data[0][1] <= current_time:
            score, time, pin = heapq.heappop(self.data)
            if -score > best_score:  # Negate score to get original value
                best_score = -score
                best_pin = pin

        return best_pin

