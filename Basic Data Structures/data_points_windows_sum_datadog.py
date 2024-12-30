"""
# input_points = [
#     {"tags": ["env:dev"], "timestamp": 0, "value": 1},
#     {"tags": ["env:dev"], "timestamp": 1, "value": 3}, 
#     {"tags": ["env:prod", "host:a"], "timestamp": 2, "value": 5},
#     {"tags": ["env:dev"], "timestamp": 3, "value": -1},
#     {"tags": ["env:dev", "host:a"], "timestamp": 6, "value": -3},
#     {"tags": ["env:dev"], "timestamp": 7, "value": 5},
#     {"tags": ["env:staging", "host:a"], "timestamp": 9, "value": -3},
#     {"tags": ["env:dev"], "timestamp": 10, "value": -4},
#     {"tags": ["env:dev"], "timestamp": 11, "value": 6},
#     {"tags": ["env:dev"], "timestamp": 14, "value": -1},
#     {"tags": ["env:staging"], "timestamp": 15, "value": 10}
# ]

function that takes an input list of datapoints, a tag t, and an integer k (window length in number of points)
and return the computed sums of each consecutive window of size k for all datapoints associated with tag t.
A datapoint is associated with tag t if the tag is included along with the datapoint
"""
def compute_window_sums(datapoints, tag, k):
    """
    O(nk) ~ o(n^2) due to .pop(0)
    O(n) for results, filtered, etc
    Computes the sums of each consecutive window of size k for datapoints associated with the given tag.
    :param datapoints: List of dictionaries, each containing 'tags', 'timestamp', and 'value'.
    :param tag: The tag to filter datapoints by.
    :param k: The window size (number of points).
    :return: List of sums for each window.
    """
    # Filter datapoints that contain the specified tag
    filtered = [dp for dp in datapoints if tag in dp.get('tags', [])]
    # Optional: Sort the filtered datapoints by timestamp to ensure correct order
    # filtered.sort(key=lambda x: x['timestamp'])
    window_sums = []
    current_sum = 0
    window = []
    for dp in filtered: 
        """
        for each data point we check, if we've seen k datapoints before (including this one)
        if yes, build an answer 
        """
        window.append(dp['value'])  # adds a value
        current_sum += dp['value']  # running_sum
        
        if len(window) == k:  # found what we need
            window_sums.append(current_sum) # building the result
            # Remove the first element from the window
            removed = window.pop(0)
            current_sum -= removed # and from the rolling sum 
    return window_sums

def compute_window_sums_deque(datapoints, tag, k):
    """
    same as above but removing from deque() should be cheaper
    O(n) for the loop, since .popleft() is O(1)
    O(n)
    """
    # Filter datapoints that contain the specified tag
    filtered = [dp for dp in datapoints if tag in dp.get('tags', [])]
    
    # Sort the filtered datapoints by timestamp to ensure correct order
    filtered.sort(key=lambda x: x['timestamp'])
    
    window_sums = []
    current_sum = 0
    window = deque()  # change from above
    
    for dp in filtered:
        # Add the new value to the window and update the sum
        window.append(dp['value'])
        current_sum += dp['value']
        
        if len(window) == k:
            # Record the sum of the current window
            window_sums.append(current_sum)
            
            # Remove the oldest value from the window
            current_sum -= window.popleft()  # change from above 
    return window_sums

"""
Instead of looking at a window composed of k timestamps, we'd like to
have sliding windows that are k seconds long. We want each window to start at a
timestamp in the filtered input, and end k seconds later, so long as the window
is fully contained within the time range of the input data.
"""

from collections import deque

def compute_window_sums_by_time(datapoints, tag, k):
    """
    O(n) both 
    Computes the sums of values in sliding windows of k seconds for datapoints associated with the given tag.

    :param datapoints: List of dictionaries, each containing 'tags', 'timestamp', and 'value'.
    :param tag: The tag to filter datapoints by.
    :param k: The window length in seconds.
    :return: List of sums for each window.
    """
    # Filter datapoints that contain the specified tag
    filtered = [dp for dp in datapoints if tag in dp.get('tags', [])]
    
    # Sort the filtered datapoints by timestamp to ensure correct order
    filtered.sort(key=lambda x: x['timestamp'])
    
    # Initialize the result list and the deque for the sliding window
    window = deque()
    window_sums = []
    current_sum = 0
    
    for dp in filtered:
        start_time = dp['timestamp']
        
        # Add the current point to the window
        window.append(dp)
        current_sum += dp['value']
        
        # Remove points that fall outside the k-second window
        while window and window[0]['timestamp'] < start_time - k:
            current_sum -= window.popleft()['value']
        
        # Record the sum if the window is within bounds
        if window and window[-1]['timestamp'] <= start_time + k:
            window_sums.append(current_sum)
    
    return window_sums

