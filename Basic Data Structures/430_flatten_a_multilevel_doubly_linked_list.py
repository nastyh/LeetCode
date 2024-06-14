"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        recursive, O(n) and O(1)
        """
       def _helper(node, bottom, _next):
            curr = bottom
            while curr.next:
                if curr.child:
                    _helper(curr, curr.child, curr.next)
                curr = curr.next
            node.next = bottom
            bottom.prev = node
            node.child = None
            curr.next = _next
            if _next:
                _next.prev = curr
        
        temp = head
        while temp:
            if temp.child:
                _next = temp.next
                _helper(temp, temp.child, _next)
            temp = temp.next
        return head

    def flatten_dfs(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        def dfs(node):
            if node.child: #if node has a child, we go down
                temp = node.next # store the next node to temp 
                node.next = node.child # current node's next points to its child 
                node.child.prev = node # current node's child's prev points to current node
                last = dfs(node.child) # dfs the list that starts with current node's child (i.e., list with one level down), this will return the end node of the list one level below
                node.child = None # assign null to child
                if temp and last: # if the original next node is not null and the last node of the list one level below are both not null, we should connect them
                    last.next = temp
                    temp.prev = last
                    return dfs(temp) # after connection, we should keep searching down the list on the current level
                else: # if the original next node is Null, we can't append it to our current list. As a result, we can simply return the last node from below so we can connect it with the list one level above. 
                    return last 
                
            elif node.next: # if there is a next element, go right
                return dfs(node.next)
            else: # we've hit the end of the current list, return the last node
                return node
            
        dfs(head)
        return(head)