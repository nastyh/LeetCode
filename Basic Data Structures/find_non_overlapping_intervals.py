def find_non_overlapping_intervals(intervals):
    """
    O(nlogn) and O(n)
    """
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    res = []
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        # If there's a gap between previous end and current start
        if current_start > prev_end:
            res.append([prev_end, current_start])
        # Update the previous end to the maximum end so far
        prev_end = max(prev_end, current_end)
    return res