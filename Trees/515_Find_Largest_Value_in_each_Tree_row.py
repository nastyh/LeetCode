# Definition for a binary tree node.
from collections import deque, defaultdict
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def largestValues(self, root):
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            values_in_level = []
            for _ in range(len(q)):
                t = q.popleft()
                values_in_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(values_in_level)
        return [max(i) for i in res]


    def largestValues_optimal(self, root): # without keeping the whole level of values in a given level O(n) and O(d) where d is the level of the tree
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            curr_res = -math.inf
            for _ in range(len(q)):
                t = q.popleft()
                curr_res = max(curr_res, t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(curr_res)
        return res

    
    def largestValues_DFS(self, root): # using a dictionary, takes O(n) space
        if not root:
            return []
        self.d = defaultdict(list)
        def _helper(root, level):
            if not root: return
            self.d[level].append(root.val)
            if root.left:
                _helper(root.left, level + 1)
            if root.right:
                _helper(root.right, level + 1)
        _helper(root, 1)
        return [max(i) for i in self.d.values()]
        

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(3)
    l.right = TreeNode(2)
    l.left.left = TreeNode(5)
    l.left.right = TreeNode(3)
    # l.right.left = TreeNode(5)
    l.right.right = TreeNode(9)

print(l.largestValues(l))
print(l.largestValues_optimal(l))
print(l.largestValues_DFS(l))

