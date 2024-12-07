class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        O(nlog(m)), where n = len(weights) 
        m = sum(weights) - max(weights), is the size of the search space
        O(1)
        need to start with the largest item and check if it can be shipped within
        a provided number of days given the max capacity (max(weights))
        """
        def _helper(candidate):
            """
            returns whether we can ship a current weight within
            a provided number of days
            """
            curr_total = 0
            days_needed = 1
            for weight in weights: 
                curr_total += weight
                if curr_total > candidate:
                    curr_total = weight
                    days_needed += 1
            return days_needed <= days
        l, r = max(weights), sum(weights) 
        while l < r: 
            m = l + (r - l) // 2
            if _helper(m):
                r = m
            else:
                l = m + 1
        return l