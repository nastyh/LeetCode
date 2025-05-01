import bisect
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        n - tasks, m - workers
        Sorting: O(nlogn + mlogm)
        Binary search: O(log(min(m,n)))
        Total: O((n+m)*log(n+m) + min(n,m)*log(m,n))
        Space: O(n+m) for sorting 

        “binary‐search + greedy‐check” problem. We’ll binary‐search on the number of tasks, k,
        that we can possibly complete; for each candidate, k, we check in O(k) 
        (after sorting) whether it’s doable with at most pills of bonus strength
        """
        tasks.sort()
        workers.sort()

        def can(k: int) -> bool:
            # pick k easiest tasks + k strongest workers
            T = tasks[:k]
            W = workers[len(workers)-k:]
            pills_left = pills
            # use a list for W
            for t in reversed(T):
                # try without pill
                if W[-1] >= t:
                    W.pop()
                else:
                    # need to use pill
                    if pills_left == 0:
                        return False
                    # find worker with w+strength>=t: w>=t-strength
                    needed = t - strength
                    idx = bisect.bisect_left(W, needed)
                    if idx == len(W):  # no such worker
                        return False
                    # assign that worker
                    W.pop(idx)
                    pills_left -= 1
            return True
        

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        
        return low
    
    def maxTaskAssign_manual_bisect(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        same as above but implemented bisect_left manually 
        """

        tasks.sort()
        workers.sort()

        def _bisect_left(a, x):
            """
            finds an insertion point for x in a 
            to maintain a sorted order
            """
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def can(k: int) -> bool:
            # pick k easiest tasks + k strongest workers
            T = tasks[:k]
            W = workers[len(workers)-k:]
            pills_left = pills
            # use a list for W
            for t in reversed(T):
                # try without pill
                if W[-1] >= t:
                    W.pop()
                else:
                    # need to use pill
                    if pills_left == 0:
                        return False
                    # find worker with w+strength>=t: w>=t-strength
                    needed = t - strength
                    idx = _bisect_left(W, needed)
                    if idx == len(W):  # no such worker
                        return False
                    # assign that worker
                    W.pop(idx)
                    pills_left -= 1
            return True
        

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1
        
        return low
