from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# DFS
    def connect(self, root):
        def _helper(root, n = None):
            if not root: return
            root.next = n
            _helper(root.left, root.right)
            _helper(root.right, n.left if n else None)
            return root

        return _helper(root)

    def connect_BFS(self, root):
        """
        Keep track of the previous (on this level node)
        If the previous node exists, connect it to the current node
        Otherwise, connect the current node to None 
        """
        if not root: return
        q = deque([root])
        while q:
            size = len(q)
            nxt = None
            for i in range(size):
                node = q.popleft()
                node.next = nxt
                nxt = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root

