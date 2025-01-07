"""
List-like data structure where you can set a value at arbitrary indexes, and get the values from a range
"""
class SparseList:
    def __init__(self):
        self.data = {}

    def set(self, index, value):
        """
        Set a value at the given index.
        """
        if value is None:
            # If value is None, treat it as removing the index.
            self.data.pop(index, None)
        else:
            self.data[index] = value

    def get(self, index):
        """
        Get the value at a given index. Returns None if index is not set.
        """
        return self.data.get(index, None)

    def get_range(self, start, end):
        """
        Get the values for all indices in the range [start, end).
        Missing indices are filled with None.
        """
        return [self.data.get(i, None) for i in range(start, end)]

    def __str__(self):
        """
        String representation of the SparseList.
        """
        return f"SparseList({self.data})"

# Example usage
sparse_list = SparseList()

# Set values
sparse_list.set(10, "a")
sparse_list.set(20, "b")
sparse_list.set(15, "c")

# Get values at specific indexes
print(sparse_list.get(10))  # Output: "a"
print(sparse_list.get(25))  # Output: None

# Get values in a range
print(sparse_list.get_range(10, 20))  # Output: ["a", None, None, None, None, "c", None, None, None, None]

# Remove a value by setting it to None
sparse_list.set(15, None)
print(sparse_list.get_range(10, 20))  # Output: ["a", None, None, None, None, None, None, None, None, None]
