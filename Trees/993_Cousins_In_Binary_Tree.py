# cousing are nodes that have the same depth but different parents

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: # bfs
        
        # first we need a function that will return a depth and a parent of a given node
        
        def _parent(root, value_to_find, parent_val):
            if not root:
                return None, parent_val
            
            q = deque()
            q.append([root, parent_val])
            level = 1
            
            while q:
                for _ in range(len(q)):
                    t = q.popleft()
                    if t[0].val == value_to_find:
                        return depth, t[1]
                    if t[0].left:
                        q.append([t[0].left, t[0].val])
                    if t[0].right:
                        q.append([t[0].right, t[0].val])
                    level += 1 
            return level, t[1]
        
        x_depth, x_parent = _parent(x, None)
        y_depth, y_parent = _parent(y, None)
        
        if x_depth == y_depth and x_parent != y_parent:
            return True
        else:
            return False 
                    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: # recursively
         
        def _findRec(root, value_to_find, curr_depth, curr_parent):
            if not root:
                return False
            if rpot.val == x:
                return curr_depth, curr_parent
            if value_to_find < root.val:
                return _findRec(root.left, value_to_find, curr_depth + 1, curr_parent)
            if value_to_find > root.val:
                return _findRec(root.right, value_to_find, curr_depth + 1, curr_parent)
            
        x_depth, x_parent = _findRec(root, x, 0, None)
        y_depth, y_parent = _findRec(root, y, 0, None)
        
        if x_depth == y_depth and x_parent != y_parent:
            return True
        else:
            return False 
                   