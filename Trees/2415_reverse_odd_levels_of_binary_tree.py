# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        O(n) both: traverse and queue 
        the thing is that you need to return the root, not just a list with values
        So we cannot just create a list of lists and reverse each odd index
        We do the usual BFS, create level and swap the value using temp
        """
        if root and not root.left and not root.right: return root
        level = 0
        d = deque()
        d.append(root)
        while d:
            d_size = len(d)
            curr_nodes = []
            for _ in range(d_size):
                t = d.popleft()
                curr_nodes.append(t)
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            if level % 2 == 1:
                l, r = 0, len(curr_nodes) - 1
                while l < r:
                    tmp = curr_nodes[l].val 
                    curr_nodes[l].val = curr_nodes[r].val
                    curr_nodes[r].val = tmp 
                    l += 1
                    r -= 1
            level += 1
        return root

    def reverseOddLevels_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        as above but recursively in a DFS manner 
        """
        def _helper(l, r, level):
            if not l and not r: return 
            if level % 2 == 1: # doesn't pass w/ 1 but should 
                tmp = l.val
                l.val = r.val
                r.val = tmp 
            _helper(l.left, r.right, level + 1)
            _helper(l.right, r.left, level + 1)
        _helper(root.left, root.right, 0)
        return root 
