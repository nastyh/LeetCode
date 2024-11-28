# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # O(n) and O(1)
        # if we do in order traversal (left, node, right) in a BST 
        # and save the values, the list should be strictly increasing 
        # we don't need the whole list, we can run our traversal exactly k times
        self.ans = -1
        self.k = k
        def helper(root):
            if not root:
                return                    
            helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return            
            helper(root.right)
        helper(root)
        return self.ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # keep building the list: O(n) both
        # it's a bit easier to comprehend
        res = []
        if not root: return []
        def _helper(node):
            if not node: return
            _helper(node.left)
            if len(res) == k: # the last element right now is the answer 
                return 
            res.append(node.val)
            _helper(node.right)
        _helper(root)

    def kthSmallest_heap(self, root: Optional[TreeNode], k: int) -> int: 
        """
        Traverse everything blindly
        keap the heap
        take the k-th smallest element
        O(nlogk)
        O(n)
        """
        h = []
        if not root: return []
        def _helper(node, h, k):
            if not node: return
            heapq.heapify(h)
            heapq.heappush(h, node.val)
            if node.left:
                _helper(node.left, h, k)
            if node.right:
                _helper(node.right, h, k)
        _helper(root, h, k)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h))
        return res[-1]

    def kthSmallest_heap_optimized(self, root: Optional[TreeNode], k: int) -> int: # keep building the list: O(n) both
        """
        Traverse but always keep the h of the size <= k
        So we always have no more than k smallest elements we've seen so far
        do it by changing the sign of the input
        O(nlogk)
        O(n)
        """
        h = []
        if not root: return []
        def _helper(node, h, k):
            if not node: return
            heapq.heapify(h)
            if len(h) < k:
                heapq.heappush(h, -node.val) # the largest value is on top
            else: 
                heapq.heappushpop(h, -node.val) # get rid of it so we only actually have the actual largest values
            if node.left:
                _helper(node.left, h, k)
            if node.right:
                _helper(node.right, h, k)
        _helper(root, h, k)
        return -h[0] # it's the k-th smallest element in the heap, but with an opposite sign it's the k-largest 


