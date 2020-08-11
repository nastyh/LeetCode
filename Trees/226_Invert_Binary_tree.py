# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root): # long recursion
        if not root:
            return None
        if root and (not root.left and not root.right):
            return root
        if root.left and not root.right:
            return None
        if not root.left and root.right:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


    def invertTree_stack(self, root):  # using a stack
        if not root: return
        st = []
        st.append(root)
        while st:
            t = st.pop()
            if t:
                t.left, t.right = t.right, t.left
                st.append(t.left)
                st.append(t.right)
        return root


    def invertTree_bfs(self,root):  # using a queue
        if not root:
            return None
        s = deque()
        s.append(root)
        while s:
            t = s.popleft()
            if t:
                t.left, t.right = t.right, t.left
                s.extend([t.right, t.left])

        return root


    def invertTree_recur(self, root):  # short recursion
        if not root: return
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree_recur(root.left)
            self.invertTree_recur(root.right)
        return root


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(7)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(6)
    l.right.left = TreeNode(3)
    l.right.right = TreeNode(1)
    # l.right.right = TreeNode(18)

print(l.invertTree(l))
print(l.invertTree_bfs(l))
print(l.invertTree_stack(l))
print(l.invertTree_recur(l))
