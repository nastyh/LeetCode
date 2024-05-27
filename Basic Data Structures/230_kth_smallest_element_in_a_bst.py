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


