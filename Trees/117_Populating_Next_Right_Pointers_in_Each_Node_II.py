
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque

    def connect(self, root):
        if root ==  None:
            return None
        q = deque([root])
        while q:
            size = len(q)
            while size > 0:
                node = q.popleft()
                if size > 1 :
                    node.next = q[0]
                size -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
    

    def connect_prev(self, root):  # easier to comprehend  O(n) and O(n)
        """
        Maintain prev as a node. If it exists, then point prev.next to the current node.
        Otherwise, do nothing
        """
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


    def connect_w_linked_list(self, root):  # O(n) and O(1)
        def processChild(childNode, prev, leftmost):  # helper func
            if childNode:
                # If the "prev" pointer is alread set i.e. if we
                # already found atleast one node on the next level,
                # setup its next pointer
                if prev:
                    prev.next = childNode
                else:    
                    # Else it means this child node is the first node
                    # we have encountered on the next level, so, we
                    # set the leftmost pointer
                    leftmost = childNode
                prev = childNode 
            return prev, leftmost
        if not root:
            return root
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = processChild(curr.left, prev, leftmost)
                prev, leftmost = processChild(curr.right, prev, leftmost)
                # Move onto the next node.
                curr = curr.next         
        return root 
        
       