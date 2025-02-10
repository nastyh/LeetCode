import heapq

class Solution:
    def getKth_dp(self, lo: int, hi: int, k: int) -> int:
        """
        O((hi−lo+1)log(max(hi))+(hi−lo+1)logk)
        O(k) for heap
        save in a dictionary what has already been calculated 
        """
        dp = {}
        h = []
        def _helper(x):
            if x == 1: 
                return 0
            if x in dp:
                return dp[x]
            if x % 2 == 0:
                dp[x] = 1 + _helper(x//2)
            else:
                dp[x] = 1 + _helper(3*x+1)
            return dp[x]
        for i in range(lo, hi+1):
            curr_power = _helper(i)
            heapq.heappush(h, (-curr_power, -i))
            if len(h) > k:
                heapq.heappop(h)
        return -h[0][1]

    def getKth_heap(self, lo: int, hi: int, k: int) -> int:
        """
        Maintain a heap of size k
        O((hi-lo+1)*log(max(power)))
        O(k) due to heap 
        """
        h = []
        def _helper(x):
            res = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                res += 1
            return res 
        for i in range(lo, hi + 1):
            curr_power = _helper(i)
            heapq.heappush(h, (-curr_power, -i))
            if len(h) > k:
                heapq.heappop(h)
        res = sorted((-curr_power, -i) for curr_power, i in h)
        return res[k-1][1]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        O((hi-lo+1)*log(max(h_i))) for power computation
        plus 
        O((hi-lo+1)*log(hi-lo+1)) for sorting
        O(hi-lo+1) is space for candidates

        Just calculate the powers for the numbers 
        using _helper
        store tuples: number, its power
        sort 
        return the k-th element 
        """
        def _helper(x):
            res = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                res += 1
            return res 
        candidates = [(i, _helper(i)) for i in range(lo, hi + 1)]
        candidates.sort(key=lambda x: (x[1], x[0]))
        return candidates[k-1][0]