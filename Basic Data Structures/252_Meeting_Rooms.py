def canAttendMeetings_optimal(intervals):  # O(nlogn) and O(1)
    intervals.sort(key = lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True


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


def canAttendMeetings_alt(intervals):
    """
    More straightforward:
    sort the list, put the first element into control
    If end of control > start of the next one: False
    otherwise, make the end of control equal to the end of the next one
    """
    if len(intervals) <= 1: return True
    intervals.sort(key = lambda x: x[0])
    control = intervals[0]
    for i in range(1, len(intervals)):
        if control[1] > intervals[i][0]:
            return False
        else:
            control[1] = intervals[i][1]
    return True
    

if __name__ == '__main__':
    print(canAttendMeetings([[0, 30],[5, 10],[15, 20]]))
    print(canAttendMeetings_alt([[0, 30],[5, 10],[15, 20]]))
    print(canAttendMeetings([[7,10],[2,4]]))
    print(canAttendMeetings_alt([[7,10],[2,4]]))