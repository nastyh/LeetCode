import heapq
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def findSecondMinimumValue_heap(root):  # O(klogk) both 
        """
        Collect values into res
        Then add unique values into h.
        Heapify and return second smallest value 
        """
        res = []
        def _helper(node):
            if not node: return
            _helper(node.left)
            res.append(node.val)
            _helper(node.right)
        _helper(root)
        if len(set(res)) == 1: return -1
        h = []
        for val in set(res):
            h.append(val)
        heapq.heapify(h)
        heapq.heappop(h)
        return heapq.heappop(h)

    
    def findSecondMinimumValue_brute_force(root):  # O(N) both 
        """
        Traverse, add to the set
        The first min is the root value 
        Look for the second min
        """
        def dfs(node):
            if node:
                uniques.add(node.val)
                dfs(node.left)
                dfs(node.right)
        uniques = set()
        dfs(root)
        min1, ans = root.val, float('inf')
        for v in uniques:
            if min1 < v < ans:
                ans = v
        return ans if ans < float('inf') else -1


    def findSecondMinimumValue_optimized(root):  # O(N) both 
        """
        When traversing the tree at some node,  if node.val > min1, we know all values in the subtree at
        node are at least node.val, so there cannot be a better candidate for the second minimum in this subtree. Thus, we do not need to search this subtree.
        """
        ans = float('inf')
        min1 = root.val
        def dfs(node):
            if node:
                if min1 < node.val < ans:
                    ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return ans if ans < float('inf') else -1

    
    def findSecondMinimumValue_bfs(root):
        result = []
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if len(sorted(set(result))) == 1:
            return -1
        return sorted(set(result))[1]