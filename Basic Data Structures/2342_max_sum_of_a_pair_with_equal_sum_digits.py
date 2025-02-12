from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        O(nlogn) for sor
        O(n) for dict
        Create a dict
        sum of digits in a num: [these nums]
        if >=2 in a list, sort, take first two
        sum, compare to glob_res, build the result
        """
        d = defaultdict(list)
        glob_res = -1
        for n in nums:
            s = sum(map(int, str(n)))
            d[s].append(n)
        for s, arr in d.items():
            if len(arr) >= 2:
                arr.sort(reverse=True)
                curr_sum = arr[0] + arr[1]
                glob_res = max(glob_res, curr_sum)
        return glob_res 
    
    def maximumSum_heap(self, nums: List[int]) -> int:
        """
        O(nlogm), m is the ave num of digits
        O(logm) for heap
        """
        d = defaultdict(list)
        glob_res = -1
        for n in nums:
            ds = sum(map(int, str(n)))
            heapq.heappush(d[ds], -n)
        for ds, h in d.items():
            if len(h) >= 2:
                first = -heapq.heappop(h)
                second = -heapq.heappop(h)
                glob_res = max(glob_res, first+second)
        return glob_res
        