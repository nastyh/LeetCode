import heapq
class Solution:
    def twoCitySchedCost_sorting(self, costs: List[List[int]]) -> int: # O(nlogn) and O(1)
        a = sorted(costs, key = lambda x: x[0]-x[1]) # sort by the difference between the prices
        # List with the lowest first prices will go first
        Sb = 0
        for i in range(len(a) // 2): # guarantees we pick a half of costs that are min 
            Sa += a[i][0] # to start somewhere
        for i in range(len(a) // 2, len(a)):
            Sb += a[i][1]
        return Sa + Sb

    def twoCitySchedCost_minheap(self, costs: List[List[int]]) -> int: # O(n) both
        # assume everyone goes to A first. 
        # min heap stores the diff between second and first, sorted by this diff
        # first half of the heap will show whether going to B is better
        # in this case the difference will be negative
        # if we overcount, we now will substract 
        # others will go to B regardless
        diff, res = [], 0
        for i in range(len(costs)):
            res += costs[i][0]  # everyone goes to A first
            heapq.heappush(diff, costs[i][1] - costs[i][0]) # list of differences, for each element
        for _ in range(len(costs) // 2): # the first half of the heap
            res += heapq.heappop(diff)
        return res 




    