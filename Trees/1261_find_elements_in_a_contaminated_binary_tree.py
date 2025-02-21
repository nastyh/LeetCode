# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        BFS
        O(N) for findelements to do a BFS
        O(1) to find since it's a set
        O(N) to save all the values in the set
        """
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self._helper(root, 0)  # don't forget to pass it here
        self._dfs(root) # it's the second solution 
    
    def _helper(self, node, curr_val):
        """
        need curr_val so that we change root.val to zero 
        from here, just throw the value into the set
        call recursively on both children
        """
        if not node: return 
        self.values.add(curr_val)
        """
        we can add if node.left: and if node.right in front 
        of the _helper calls 
        """
        self._helper(node.left, curr_val * 2 + 1)
        self._helper(node.right, curr_val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.values
    

    #  BFS
    def _bfs(self, node):
        """
        Normal bfs 
        just update the first node value to 0
        then process one by one
        throw the current value into the seen set 
        update the values of the children 
        put them back in the deque 
        """
        d = deque()
        node.val = 0 
        d.append(node)
        while d:
            curr = d.popleft()
            self.values.add(curr.val)
            if curr.left:
                curr.left.val = curr.val * 2 + 1
                d.append(curr.left)
            if curr.right:
                curr.right.val = curr.val * 2 + 2
                d.append(curr.right)




# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)