"""
Each task has a start and an end time [start, end] where end > start. Find out for the given schedule:

in what intervals you are working (at least 1 task ongoing)
in what intervals you are multitasking (at least 2 tasks ongoing)
In other words, find union and intersection of a list of intervals. The input is sorted by start time.

Example:
Input: [[1, 10], [2, 6], [9, 12], [14, 16], [16, 17]]

Output union: [[1, 12], [14, 17]]
Explanation: We just need to merge overlapping intervals https://leetcode.com/problems/merge-intervals

Output intersection: [[2, 6], [9, 10]]
"""

def interval_intersections(intervals):
    if not intervals:
        return []
    intervals.sort()
    ans = []
    prev = intervals[0]
    for start, stop in intervals[1:]:
        prev_start, prev_stop = prev
        lo = max(start, prev_start)
        hi = min(stop, prev_stop)
        if lo < hi: # intersection found
            if ans and ans[-1][1] == lo: # merge intersection with previous intersection if needed
                ans[-1][1] = hi
            else:
                ans.append([lo, hi])
            prev = [hi, max(stop, prev_stop)] # important part
        else:
            prev = [start, stop]
    return ans