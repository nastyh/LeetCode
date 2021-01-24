from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# DFS  a
    def connect(self, root):  # O(N) and O(h)
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


    def connect_BFS_alt(self, root):  # O(n) and O(N)
        if not root: return
        d = deque()
        d.append(root)
        while d:
            for i in range(1, len(d)):
                d[i - 1].next = d[i]
            d[-1].next = None
            next_level = deque()
            for t in d:
                if t.left:
                    next_level.append(t.left)
                if t.right:
                    next_level.append(t.right)
            d = next_level
        return root

    
    def connect_BFS_prev(self, root):  # O(n) and O(N)
        if not root: return
        d = deque()
        d.append(root) 
        while d:
            prev = None  # the key is to do this line inside the while loop, not outside
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


    def connect_efficient(self, root): # O(n) and O(1)
        if not root:
            return root
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        # Once we reach the final level, we are done
        while leftmost.left:
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                # Progress along the list (nodes on the current level)
                head = head.next
            # Move onto the next level
            leftmost = leftmost.left
        return root 

