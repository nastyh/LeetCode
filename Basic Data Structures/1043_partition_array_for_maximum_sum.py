class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        cannot do in the greedy manner 
        two pointers: l + r
        window is r - l + 1 
        curr_max is the max val we've seen so far
        curr_sum = curr_max * window 
        """
        # that will time out
        def _helper(i): # i is the left pointer
            curr_max, res = 0, 0
            for j in range(i, min(len(arr), i + k - 1)): # so that we don't fall out the bounds
                curr_max = max(curr_max, arr[j])
                window_size = j - i + 1
                res = max(res, _helper(j + 1) + curr_max * window_size)
            return res
        return _helper(0)

    def maxSumAfterPartitioning_caching(self, arr: List[int], k: int) -> int:
        """
        some memoization 
        i is the left pointer 
        j is in the right pointer that is i + k ideally
        but we need to take care of the end of the list so we take min in the loop
        """
        cache = {}
        def _helper(i):
            curr_max, res = 0, 0
            if i > len(arr):
                return 0
            if i in cache:
                return cache[i]
            curr_max, res = 0, 0
            for j in range(i, min(len(arr), i + k)): # so that we don't fall out the bounds
                curr_max = max(curr_max, arr[j])
                window_size = j - i + 1
                # curr_max * window_size maximises the potential result 
                res = max(res, _helper(j + 1) + curr_max * window_size)
            cache[i] = res
            return res
        return _helper(0)

    def maxSumAfterPartitioning_dp(self, arr: List[int], k: int) -> int:
        """
        O(Nk) and O(k)
        """
        dp = [0] * k
        dp[0] = arr[0]
        max_at_i = 0
        for i in range(1, len(arr)):
            curr_max = 0
            for j in range(i, i - k, -1): # window to the left 
                if j < 0:  # don't go out of bounds
                    break 
                curr_max = max(curr_max, arr[j])
                window_size = i - j + 1
                curr_sum = curr_max * window_size
                sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1] # result of the sub problem
                max_at_i = max(max_at_i, curr_sum + sub_sum)
            dp[i % k] = max_at_i
        return dp[(len(arr) - 1) % k]

