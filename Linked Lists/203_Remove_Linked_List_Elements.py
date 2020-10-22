def removeElements(head, val):
    dummy = ListNode(-1)
    dummy.next = head # create a dummy variable that stands before head
    curr = dummy # curr becomes a dummy var
    while curr.next:
        if curr.next.val == val: # if the next node is the number we want to remove
            curr.next = curr.next.next # relinking one node forward
        else:
            curr = curr.next # otherwise keep moving 
    return dummy.next


def removeElements_easy(head, val):
    if not head: return
    prev, curr = None, head
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
        else:
            prev = curr
        curr = curr.next
    return head


def removeElements_recursive(head, val):
    def _helper(node, val):
        if node:
            if node.val == val:
                return _helper(node.next, val)
            else:
                node.next = _helper(node.next, val)
        return node
    return _helper(node, val)
    
    