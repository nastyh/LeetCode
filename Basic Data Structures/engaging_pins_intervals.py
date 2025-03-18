"""
Pins, their start time and end time 
They might overlap 
Return each interval's start and end times and the number of pins happening within this interval
Input is 
input = [
#     ["pinA", 0, 5],
#     ["pinB", 1, 2],
#     ["pinC", 3, 7]
# ]

time line 
0-->1-->2-->3-->5-->7
  1   2   1   2   1   <-- these are active pins within this interval

Output is
[[0, 1, 1], [1, 2, 2], [2, 3, 1], [3, 5, 2], [5, 7, 1]]

"""
def pin_intervals(pins):
    """
    O(mlogm) m is the num of unique times.
    If times are seconds [0; 59], it's pretty much O(1)
    O(n) for the dict and res in the worst case 
    """
    d = {}
    res, curr_count, prev_time = [], 0, None
    for name, st, end in pins:
        d[st] = d.get(st, 0) + 1
        d[end] = d.get(end, 0) - 1 
    sorted_times = sorted(d.keys())
    for time in sorted_times:
        if prev_time is not None: 
            if curr_count > 0: 
                res.append([prev_time, time, curr_count])
        curr_count += d[time] 
        prev_time = time 
    return res 

"""
Follow-up 
if times are in seconds, zero to 59. Can we do it without a dictionary and sorting
but rather with a list of 60 elements?
"""
def pin_intervals_no_sort(pins):
    """
    O(n+t), where n is the num of intervals, T is the max time in seconds (59)
    O(t) for d, but it's only 60, so it's O(1)
    """
    d = [0] * 60 # list of the size of max_time + 1. Max_time is 59 
    # mark the changes in the number of active pins at each second 
    for _, st, end in pins:
        d[st] += 1
        if end < len(d): # check so that we don't go out of bounds of 59 
            d[end] -= 1
    res, curr_count, segment_start = [], d[0], 0 
    for t in range(60):
        new_count = curr_count + d[t]
        # If the count changes, record the segment from segment_start to t if active.
        if new_count != curr_count:
            if curr_count > 0: 
                res.append([segment_start, t, curr_count])
            segment_start = t
        curr_count = new_count
    return res 