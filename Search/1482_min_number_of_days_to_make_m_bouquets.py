class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        O(nlogn), n is len(bloomDay)
        O(1)
        Are there enough flowers when all bloom?
        What is the minimum and maximum day?
        Is the possibility to collect the bouqets monototically?
        Use the binary search to search all possible days.
        As every search step, iterate ones over the array trying to collect the flowers.
        """
        if m * k > len(bloomDay): return -1 # edge case, not enough flowers to work with
        l, r = 0, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            bouquet_number = 0
            count_number = 0
            for b in bloomDay:
                if b <= mid:
                    count_number += 1
                    if count_number == k: 
                        count_number = 0 
                        bouquet_number += 1
                        if bouquet_number == m:
                            break 
                else:
                    count_number = 0
            else:
                l = mid + 1 
                continue 
            r = mid 
        return l
