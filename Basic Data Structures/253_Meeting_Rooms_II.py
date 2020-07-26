def minMeetingRooms(intervals):
    rooms = 1
    if len(intervals) == 0: return 0
    if len(intervals) == 1: return rooms
    intervals.sort(key = lambda x: x[0])
    return intervals
    for ix in range(len(intervals) - 1):
        if intervals[ix][1] > intervals[ix + 1][0]:
            rooms += 1
    return rooms


if __name__ == '__main__':
    print(minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
    