
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque
class Solution:
    def connect(self, root):
        if root ==  None:
            return None
        q = deque([root])
        while q:
            size = len(q)
            while size > 0:
                node = q.popleft()
                if size > 1 :#
                    node.next = q[0]
                size -= 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
    

    def connect_prev(self, root):  # easier to comprehend
        """
        Maintain prev as a node. If it exists, then point prev.next to the current node.
        Otherwise, do nothing
        """
        if not root: return
        d = deque()
        d.append(root) 
        while d:
            prev = None
            for _ in range(len(d)):
                t = d.popleft()
                if prev:
                    prev.next = t
                prev = t
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
        return root

