# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def minDepth(self, root):
        if not root: return 0
        res = 1
        if root and not root.left and not root.right: return res

        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


    def minDepth_stupid_DFS(self, root):
        if not root: return 0
        def _helper(root):
            if not root: return 0
            if root and not root.left and not root.right: return 1

            if root.left and not root.right:
                return _helper(root.left) + 1
            if not root.left and root.right:
                return _helper(root.right) + 1
            if root.left and root.right:
                return min(_helper(root.left), _helper(root.right)) + 1
        return _helper(root)


    def minDepthDFS_another(self, root):
        """
        With a tiny twist
        Start calculating the depth in a helper function
        The key here is to initialize l and r to None
        If any of these stay None, it means that there was no left (or right) tree. 
        Then in the if portion we need to handle cases when there is no subtree. We don't want to get a zero in this case.
        It handles edge cases when the whole tree is just left (or right) subtrees (like a linked list, essentially)
        """
        if not root: return 0
        if root and not root.left and not root.right: return 1
        def _helper(node, d):
            if not node: return 
            if node and not node.left and not node.right:
                d += 1
                return d
            l, r = None, None
            if node.left:
                l = _helper(node.left, d)
            if node.right:
                r = _helper(node.right, d)
            # this stupid portion is required to handle edge cases when a tree has only left (or right) children
            if l is not None and r is not None:
                return min(l, r) + 1
            if l is None and r is not None:
                return r + 1
            if l is not None and r is None:
                return l + 1
        return _helper(root, 0)


    def minDepthDFS(self, root):
        if not root: return 0
        l = self.minDepthDFS(root.left)
        r = self.minDepthDFS(root.right)

        if root.left and root.right:
            return min(l, r) + 1
        elif root.left:
            return l + 1
        elif root.right:
            return r + 1
        else:
            return 1

    def minDepthBFS(self, root):
        if not root: return 0
        d = deque()
        d.append([root, 1])
        while d:
            t, curr_d = d.popleft()
            if not t.left and not t.right:
                return curr_d
            if t.left:
                d.append([t.left, curr_d + 1])
            if t.right:
                d.append([t.right, curr_d + 1])



if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)

    print(l.minDepth(l))
    print(l.minDepthDFS(l))
    print(l.minDepthDFS_another(l))
    print(l.minDepthBFS(l))
    print(l.minDepth_stupid_DFS(l))
