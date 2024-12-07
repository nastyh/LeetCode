
class HitCounter:
    """
    binary search
    O(nlogn) and O(1) b/c of the max size of 300 
    Since timestamps are monotonically increasing,
    we can use binary search to figure out the closest timestamp to the given timestamp in getHits()
    Once we find this, until hits until we either reach the end of the array or an element
    earlier than timestamp-300 seconds.
    """

    def __init__(self):
        self.hits = {}
        self.timeline = []

    def hit(self, timestamp: int) -> None:
        if self.hits.get(timestamp) == None:
            self.hits[timestamp] = 0
            self.timeline.append(timestamp)
        self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        binary search
        """
        l, r = 0, len(self.timeline) - 1
        while l < r:
            mid = l + (r - l) // 2
            if self.timeline[mid] == timestamp:
                l = mid
                break
            elif self.timeline[mid] <= timestamp and self.timeline[r] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        end = l if l < len(self.timeline) else l - 1
        startTime = max(0, timestamp - 300)
        res = 0
        while end >= 0:
            if self.timeline[end] <= startTime:
                return res
            res += self.hits[self.timeline[end]]
            end -= 1
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)




class HitCounter:

    """
    O(n) both 
    Append hit timestamps whenever it is generated. And perform binary search on the array
    Since timestamp is monotonically increasing, you can perform binary search on it
    Whenever new hit generated, append it to your timestamp list with corresponding timestamp value
    If you have to find number of hits in range:
    [timestamp-300 + 1, timestamp], you can perform binary search on your timestamp array
    As long as the value of median index of the binary search equal or smaller than timestamp-300, update left index
    If you can't update your left index anymore, it will be your answer
    """

    def __init__(self):
        

    def hit(self, timestamp: int) -> None:
        

    def getHits(self, timestamp: int) -> int:
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)