class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        O(nlogn) both, heap
        """
        events = []
        # new building events
        for L, R, H in buildings:
            # append start point of building
            events.append((L, -H, R)) # so it's a mean heap: left coordinate, height, right coord 
            # append end point of building
            events.append((R, 0, 0))
        events.sort() # left side of the building, height, right side
        res = [[0, 0]]
        h = [(0, float("inf"))]  # no building left in heap.
        for pos, neg_h, R in events:
            while h[0][1] <= pos:
                heapq.heappop(h)
            if neg_h != 0:
                heapq.heappush(h, (neg_h, R))
            if res[-1][1] != -h[0][0]:
                res.append([pos, -h[0][0]])
        return res[1:]