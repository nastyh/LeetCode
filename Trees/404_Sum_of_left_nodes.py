# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def sumOfLeftLeaves(self, root):  # O(N) both
        ls = 0
        if not root:
            return 0
        if root.left and (not root.left.left and not root.left.right):
            ls += root.left.val
            rs = self.sumOfLeftLeaves(root.right)
            return ls + rs
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    

    def sumOfLeftLeaves_dfs_another(self, root):
        if not root: return 0
        self.res = 0
        def _helper(root):
            if not root: return
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            _helper(root.left)
            _helper(root.right)
        _helper(root)
        return self.res

    
    def sumOfLeftLeaves_dfs_helper(self, root):  # probably the best and the fastest
        if not root: return 0
        self.res = 0
        def _helper(root, isLeft):
            if not root: return
            if isLeft and not root.left and not root.right:
                self.res += root.val
            if root.left: _helper(root.left, True)
            if root.right: _helper(root.right, False)
        _helper(root, False)
        return self.res


    def sumOfLeftLeaves_bfs_optimal(self, root):  # O(n) both
        """
        In the deck, keep the node and whether it's left. It's left, if it came to the deque
        from the earlier t.left statement.
        If it's left and no more children, add its value to res 
        """
        if not root: return 0
        d = deque()
        d.append((root, False))
        res = 0
        while d:
            for _ in range(len(d)):
                t, isLeft = d.popleft()
                if not t.left and not t.right and isLeft:
                    res += t.val
                if t.left:
                    d.append((t.left, True))
                if t.right:
                    d.append((t.right, False))
        return res
        

    def sumOfLeftLeaves_bfs(self, root):
        res = 0
        if not root:
            return 0
        q = deque()
        q.append(root)
        while q:
            t = q.popleft()
            if t.left and (not t.left.left and not t.left.right):
                res += t.left.val
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res


    def sumOfLeftLeaves_bfs_slight(self, root):
        res = 0
        if not root:
            return 0
        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            if not t.left and not t.right:
                res += t.val
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res


    def sumOfLeftLeaves_bfs_simple(self, root): # BFS but with saving the whole tree
        if not root: return 0
        res = []
        q = deque()
        q.append(root)
        while q:
            curr = []
            for _ in range(len(q)):           
                t = q.popleft()
                curr.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(curr)
        return sum([i[0] for i in res[1:]])


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.sumOfLeftLeaves(l))
    print(l.sumOfLeftLeaves_dfs_another(l))
    print(l.sumOfLeftLeaves_dfs_helper(l))
    print(l.sumOfLeftLeaves_bfs_slight(l))
    print(l.sumOfLeftLeaves_bfs(l))
    print(l.sumOfLeftLeaves_bfs_simple(l))
