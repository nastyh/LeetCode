class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        O(nlogn) and O(n)
        sort by the start time --> starts
        sort by the end time --> ends
        end intervals from ends which are < than current start
        """
        starts = sorted(events, key = lambda x: x[0])
        ends = sorted(events, key = lambda x: x[1])
        max_val, ending_ix = 0, 0
        # events.sort(key = lambda x: x[0])
        res = 0 
        for i in range(len(starts)):
            while ending_ix < len(ends) and ends[ending_ix][1] < starts[i][0]:
                max_val = max(max_val, ends[ending_ix][2])
                ending_ix += 1
            res = max(res, starts[i][2] + max_val)
        return res 

    def maxTwoEvents_heap(self, events: List[List[int]]) -> int:
        """
        O(nlogn) and O(n)
        can consider two events at a time 
        heap contains the min ending time and profit
        res1 has themaximum value among all the events
        ending before the current event starts
        res2 is the max profit we want to obtain
        """
        events.sort(key = lambda x: x[0])
        h = []
        res1, res2 = 0, 0
        for st, end, profit in events:
            while h and heap[0][0] < st: 
                res1 = max(res1, heapq.heappop(h)[1])
            res2 = max(res2, res1 + profit)
            heapq.heappush(h, (end, profit))
        return res2
