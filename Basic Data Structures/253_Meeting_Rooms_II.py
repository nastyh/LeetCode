import heapq
def minMeetingRooms(intervals):
    if len(intervals) <= 1: return len(intervals)
    start_times = [interval[0] for interval in intervals]
    end_times = [interval[1] for interval in intervals]
    start_times.sort()
    end_times.sort()
    res = 0
    end_ix = 0
    for i in range(len(intervals)):
        if start_times[i] < end_times[end_ix]:
            res += 1
        else:
            end_ix += 1
    return res


def minMeetingRooms_heap(intervals):
    if len(intervals) <= 1: return len(intervals)
    res, heap = 0, []
    intervals.sort()
    for interval in intervals:
        while heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        res = max(res, len(heap))
    return res


def minMeetingRooms_another(intervals):
    if len(intervals) <= 1: return len(intervals)
    intervals.sort(key = lambda x: x[0])
    intervals = sorted(intervals, key = lambda x: x[1], reverse = True)
    res, curr = 0, intervals[0]
    for interval in intervals[1:]:
        if interval[1] < curr[1]:
            res += 1
            curr = interval
        else:
            curr = interval
    return res

if __name__ == '__main__':
    print(minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
    print(minMeetingRooms_heap([[9, 10], [4, 9], [4, 17]]))
    print(minMeetingRooms_another([[9, 10], [4, 9], [4, 17]]))