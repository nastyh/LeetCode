"""
Implement a structure to store a rolling data
sliding windows for averages, sums, or other computations over time series data

Fixed Window Size:
The structure only retains the last N elements, discarding older elements.
Efficient Insertion:

Adding new elements should be O(1), replacing the oldest data when the window size exceeds N.
Efficient Querying:
Support operations like computing rolling sums, averages, or retrieving the full window.

circular buffer (or ring buffer) is an ideal choice for this scenario.
It maintains a fixed-size array and uses two pointers to track the head (oldest) and tail (newest)
elements. When the buffer is full, new elements overwrite the oldest.
"""
class RollingData:
    def __init__(self, size):
        """
        Initialize a rolling data structure with a fixed size.
        :param size: Maximum number of elements in the rolling window.
        """
        self.size = size
        self.data = [None] * size
        self.head = 0  # Points to the oldest element
        self.count = 0  # Number of elements in the buffer
        self.running_sum = 0 # optional

    def add(self, value):
        """
        O(1) and O(N)
        Add a new value to the rolling window.
        :param value: The new value to add.
        """
        # Insert at the current head and move the head pointer
        self.data[self.head] = value
        self.head = (self.head + 1) % self.size
        # Ensure count doesn't exceed the buffer size
        self.count = min(self.count + 1, self.size)

        # optional
        # Subtract the old value being replaced
        old_value = self.data[self.head]
        self.running_sum += value - old_value


    def get_all(self):
        """
        O(N)
        Retrieve all elements in the rolling window in order.
        :return: A list of elements in the window.
        """
        if self.count == 0:
            return []
        if self.count < self.size:
            return self.data[:self.count]
        # Return the elements in order
        return self.data[self.head:] + self.data[:self.head]

    def rolling_sum(self):
        """
        O(N)
        Compute the sum of the elements in the rolling window.
        :return: The sum of the elements.
        """
        return sum(self.get_all())

    # or 
    def rolling_sum(self):
        return self.running_sum

    def rolling_average(self):
        return self.running_sum / self.count if self.count > 0 else 0

    def rolling_average(self):
        """
        Compute the average of the elements in the rolling window.
        :return: The average of the elements.
        """
        elements = self.get_all()
        return sum(elements) / len(elements) if elements else 0


# Initialize with a rolling window size of 5
rolling_window = RollingData(5)

# Add elements
rolling_window.add(10)
rolling_window.add(20)
rolling_window.add(30)
rolling_window.add(40)
rolling_window.add(50)

# Retrieve rolling data
print("Current Window:", rolling_window.get_all())  # Output: [10, 20, 30, 40, 50]

# Add more elements (rolling behavior)
rolling_window.add(60)
rolling_window.add(70)
print("Current Window:", rolling_window.get_all())  # Output: [30, 40, 50, 60, 70]

# Compute rolling sum and average
print("Rolling Sum:", rolling_window.rolling_sum())       # Output: 250
print("Rolling Average:", rolling_window.rolling_average())  # Output: 50.0
