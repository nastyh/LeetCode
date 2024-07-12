class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Start/end times of the jobs
        Profit per job
        Maximise the profit; jobs cannot overlap
        Also similar to AirBnB rooms: one room, have reservations,
        how to make the most
        O(nlogn) due to bisect (binary search)
        O(n)
        """
        tbl = []
        for x, y, z in zip(startTime, endTime, profit):
            """
            we need to sort first by endTime, then by startTime
            so we put endTime first, then it is automatically
            the first sorting key
            """
            tbl.append([y, x, z])
            # sort first by endTime, then by startTime
        tbl.sort()
        @cache
        def dp(idx):
            if idx < 0:
                # in this case, all jobs were already considered
                # no more profit, so we return 0
                return 0 
            
            # we do not choose job No.idx, 
            # then just consider the previous job
            # ans1 is the profit we get if current job is not added
            ans1 = dp(idx-1)
             # we choose job No.idx 
            # calculate which job should be considered next 
            # nxt is the index of the next job to be considered 
            nxt = bisect_left(endTime, tbl[idx][1])
            if tbl[nxt][0] > tbl[idx][1]:
                nxt -= 1
            elif tbl[nxt][0] == tbl[idx][1]:
                nxt = bisect_right(endTime, tbl[idx][1]) - 1
            # print(nxt, tbl[nxt][0],tbl[idx][1])
            # print(nxt)
            
            # ans2 is the profit we get if current job is added
            ans2 = dp(nxt) + tbl[idx][2]
            # print("idx: ", idx, ans1, ans2)

            # compare and decide the bigger profit 
            return max(ans1, ans2)
        
        return dp(len(tbl)-1)
    
    def jobScheduling_heap(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Keep partial sums for the largest profit seen up to this time. Once you iterate past the endTime of
        a partial sum evaluate it against the current largest profit. Do this for all items where the endTime <= current startTime.
        Push this new item (endTime, maxProfit + p) to minHeap
        remember to include the profit for the current job (i.e. + p)
        O(nlogn) and O(n)
        """
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        jobs.append((maxsize, 0, 0))

        maxProfit, h = 0, []
        for s, e, p in jobs:
            while h and h[0][0] <= s:
                maxProfit = max(maxProfit, heappop(h)[1])
            heappush(h, (e, maxProfit + p))

        return maxProfit
        

    def jobScheduling_dp(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        NOT EVERYTHING PASSES
        """
        n, res = len(startTime), 0
        helper = []
        for i in range(len(startTime)):
            helper.append([endTime[i], startTime[i], profit[i]])
        helper = sorted(helper)
        dp  = [0] * len(startTime)
        dp[0] = helper[0][2] # profit from the first element
        for i in range(1, n):
            # locates the insertion point for helper[i][i] + 1 in helper so the sorting is maintained
            prevIndex=bisect.bisect_left(helper, [helper[i][1]+1])
            if prevIndex == 0:
                dp[i]=max(dp[i - 1],helper[i][2])
            else:
                dp[i]=max(dp[i - 1], dp[prevIndex - 1] + helper[i][2])
            res = max(res, dp[i])
        return res
