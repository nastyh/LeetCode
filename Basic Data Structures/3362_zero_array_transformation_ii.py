from heapq import heappop, heappush
from typing import List

def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
    """
    Optimal
    O(N + Q*logQ), N -- len(nums), Q -- len(queries), Q part for sorting the queries, then pop, single pass over nums is O(N)
    O(N+Q) diff_list is of N+1; heap grows up to Q
    
    Each element nums[i] can be decremented a total of nums[i] times.
    A query [l, r] allows us to decrement any subset of values in that interval by at most 1.

    Processes nums from left to right
    Maintains a heap of available query ranges that could still cover the current index i.
    Tracks the net effect of decrements at each index using a difference array (diffs_list).
    """
    queries.sort(key=lambda x: x[0])
    h = []
    diffs_list = [0] * (len(nums) + 1)
    operations = 0
    j = 0
    for i, num in enumerate(nums):
        operations += diffs_list[i]
        while j < len(queries) and queries[j][0] == i:
            heappush(h, -queries[j][1])
            j += 1
        while operations < num and h and -h[0] >= i:
            operations += 1
            diffs_list[-heappop(h) + 1] -= 1
        if operations < num:
            return -1
    return len(h)


def maxRemoval_binary(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Binary Search
         TIMES OUT
        """
        n = len(nums)
        m = len(queries)

        def combinations_helper(arr, k):
            """Yield all combinations of k elements from arr (like itertools.combinations)."""
            def backtrack(start, path):
                if len(path) == k:
                    result.append(path[:])
                    return
                for i in range(start, len(arr)):
                    path.append(arr[i])
                    backtrack(i + 1, path)
                    path.pop()
            result = []
            backtrack(0, [])
            return result

        def isValid(kept_indices):
            diff = [0] * (n + 1)
            for idx in kept_indices:
                li, ri = queries[idx]
                diff[li] += 1
                diff[ri + 1] -= 1
            coverage = [0] * n
            curr = 0
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True

        left, right = 0, len(queries)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            found = False
            all_indices = list(range(len(queries)))
            for remove_set in combinations_helper(all_indices, mid):
                keep_set = set(all_indices) - set(remove_set)
                if isValid(keep_set):
                    found = True
                    break
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans if ans != -1 else -1