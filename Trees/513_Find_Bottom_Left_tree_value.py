# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def findBottomLeftValue(self, root):
        from collections import deque
        if not root:
            return None
        res = []
        q = deque()
        q.append(root)
        while q:
            curr_level = []
            for _ in range(len(q)):
                t = q.popleft()
                curr_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(curr_level)
        return res[-1][0]
        
    
    def findBottomLeftValue_alt(self, root):
        """
        First, find the max depth of the tree (_helper())
        Second, do a BFS and keep track of the current depth
        Third, as soon as you see a node with the max depth, return its value
        """
        def _helper(node, d):
            if not node: return 0
            if node and not node.left and not node.right:
                return 1
            l, r = 0, 0
            if node.left:
                l = _helper(node.left, d + 1)
            if node.right:
                r = _helper(node.right, d + 1)
            return max(l, r) + 1 
        
        md = _helper(root, 0)
        d = deque()
        d.append((root, 1))
        while d:
            t, cd = d.popleft()
            if cd == md:
                return t.val
            if t.left:
                d.append((t.left, cd + 1))
            if t.right:
                d.append((t.right, cd + 1))

    
    def findBottomLeftValue_stack(self, root):
        if not root:
            return []
        head = [root]
        result = 0
        while head:
            res = []
            for nodes in head:
                if nodes.left:
                    res.append(nodes.left)
                if nodes.right:
                    res.append(nodes.right)
            if not res:
                result=head[0].val
                break
            head = res
        return result

    
    def findBottomLeftValue_DFS(self, root):
        bottom_left,max_depth = root.val, 0
        def bottom(root, depth):
            nonlocal bottom_left
            nonlocal max_depth
            if not root:
                return None
            if depth > max_depth:
                max_depth = depth
                bottom_left = root.val
            bottom(root.left, depth + 1)
            bottom(root.right, depth + 1)
        bottom(root, 0)
        return bottom_left



if __name__ == '__main__':
    l = TreeNode(2)
    l.left = TreeNode(1)
    l.right = TreeNode(3)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(6)
    print(l.findBottomLeftValue(l))
    print(l.findBottomLeftValue_alt(l))
    print(l.findBottomLeftValue_stack(l))
    print(l.findBottomLeftValue_DFS(l))