def canAttendMeetings(intervals):
    if len(intervals) <= 1: return True
    intervals.sort(key = lambda x: x[0])
    for ix in range(len(intervals) - 1):
        if intervals[ix][1] > intervals[ix + 1][0]:
            return False
        if intervals[ix][1] > intervals[ix + 1][0]:
            if intervals[ix][0] < intervals[ix + 1][0]:
                return False
    return True