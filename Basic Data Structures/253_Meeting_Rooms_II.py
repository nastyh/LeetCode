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


def minMeetingRooms_heap(intervals):  # O(nlogn) b/c of sorting and O(n) to construct a min heap that will contain the whole list in the worst case 
    """
    maintain a min heap with end times as a key. The top element is the room that will be free the earliest.
    len(heap) shows how many meetings are taking place. This is how many rooms we need
    """
    if len(intervals) <= 1: return len(intervals)
    res, heap = 0, []
    intervals.sort()
    for interval in intervals:
        while heap and heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        res = max(res, len(heap))
    return res

def minMeetingRooms_explained(self, intervals: List[List[int]]) -> int:
        """
        O(nlogn) b/c of sorting and O(n) to construct a min heap that will contain the whole list in the worst case
        maintain a min heap with end times as a key. The top element is the room that will be free the earliest.
        len(heap) shows how many meetings are taking place. This is how many rooms we need
        """
        if len(intervals) == 1: return 1
        intervals.sort()  # sort by the start time
        h, res = [], 0
        for interval in intervals:
            while h and h[0] <= interval[0]: # incoming meeting ends earlier than what we have in the heap so far
                heapq.heappop(h)
            #maintain a in heap. On top is the meeting that ends the earliest
            heapq.heappush(h, interval[1])
            res = max(res, len(h))
        return res


if __name__ == '__main__':
    print(minMeetingRooms([[9, 10], [4, 9], [4, 17]]))
    print(minMeetingRooms_heap([[9, 10], [4, 9], [4, 17]]))
