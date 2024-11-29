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
        Order jobs by either start time or end time so that overlapping jobs will be closer to each other
        We could solve the subproblem first then work toward the final solution
        O(nlogn)
        O(n)
        """
        jobs = [(a,b,c) for a,b,c in zip(startTime,endTime,profit)]
        # sort by end time
        jobs = sorted(jobs,key=lambda a:a[1])
        end_time_sorted = [a[1] for a in jobs]
        """
        dp[i] = maximum profit ending at i's end time
        dp[i] = max(dp[i-1],dp[k]+profit[i]) where k
        is the biggest index with endTime[k] <= startTime[i]
        """
        dp = [0]*(len(jobs)+1)
        for i, job in enumerate(jobs):
            start_time, end_time, p = job
            j = bisect.bisect_right(end_time_sorted, start_time, hi=i+1) #  returns an insertion point which comes after (to the right of) any existing entries of start_time in end_time_sorted.
            dp[i] = max(p, dp[i - 1], dp[j-1] + p)
        return dp[len(jobs)-1]
