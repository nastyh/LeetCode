class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        O(qlogn), q the num of queries in the queries list
        O(n+q), n for the stack, q for res and newqueries
        monotonic stack
        By traversing the heights array from right to left, we maintain a stack
        of indices in decreasing order of heights. For the current building, any
        shorter or equal buildings already in the stack cannot be the answer, so we remove them.
        If the stack is not empty, the top element gives the position of the next taller building.
        If the stack is empty, it means no taller building exists to the right, so we store -1.
        for the pairs: find the first height to the right in the heights array
        that is greater than both values in each pair.
        While traversing the heights array, we use a monotonic stack to maintain all elements
        greater than the current height, with the nearest greater height at the top of the stack.
        When processing a query, the stack already contains all elements greater than the current height.

        For each query pair, we use binary search on the stack to quickly find the first element greater 
        than the larger value in the pair. This ensures that each query is processed in O(logn) time.
        """
        def _helper(height, mono_stack):
            left = 0
            right = len(mono_stack) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if mono_stack[mid][0] > height:
                    ans = max(ans, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        mon_stack = []
        res = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                res[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            mon_stack_size = len(mon_stack)
            for a, b in new_queries[i]:
                position = _helper(a, mon_stack)
                if position < mon_stack_size and position >= 0:
                    res[b] = mon_stack[position][1]
            while mon_stack and mon_stack[-1][0] <= heights[i]:
                mon_stack.pop()
            mon_stack.append((heights[i], i))
        return res
        
