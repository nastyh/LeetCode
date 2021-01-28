# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def maxDepth(self, root):  # DFS  O(N) both
        def _helper(root):
            if not root: return 0
            if root and not root.left and not root.right: return 1
            if root.left:
                l = _helper(root.left)
            else: l = 0
            if root.right:
                r = _helper(root.right)
            else: r = 0
            return 1 + max(l, r)

        return _helper(root)


    def maxDepthBFS(self, root):  # BFS  O(N) and O(2*(log2N - 1)) ~ O(N) b/c it's the max number of nodes at a given level
        if not root: return 0
        d, levels = deque(), 0
        d.append([root, 1])
        while d:
            t, curr_l = d.popleft()
            levels = max(levels, curr_l)
            if t.left:
                d.append([t.left, curr_l + 1])
            if t.right:
                d.append([t.right, curr_l + 1])
        return levels

    
    def maxDepthBFS_minimal(self, root):  # O(n) and O(1)
        """
        Same as above but without carrying depth in a deque
        Just increment res every time you're done with a level and return at the end
        """
        if not root: return 0
        if root and not root.left and not root.right:
            return 1
        res = 0
        d = deque()
        d.append(root)
        while d:
            for _ in range(len(d)):
                t = d.popleft()
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            res += 1
        return res


    def maxDepth_helper(self, root):  # DFS but more elegant
        def _helper(root, res):
            if not root: return res
            l = _helper(root.left, res + 1)
            r = _helper(root.right, res + 1)
            return max(l, r)
        return _helper(root, 0)

    
    def maxDepth_stack(self, root):
        st = []
        if root:
            st.append((1, root))
        depth = 0
        while st:
            curr_depth, root = st.pop()
            if root:
                depth = max(depth, curr_depth)
                st.append((curr_depth + 1, root.left))
                st.append((curr_depth + 1, root.right))
        return depth 


if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.left.left = TreeNode(15)
    l.right.right = TreeNode(7)

    print(l.maxDepth(l))
    print(l.maxDepthBFS(l))
    print(l.maxDepth_helper(l))
    print(l.maxDepth_stack(l))
