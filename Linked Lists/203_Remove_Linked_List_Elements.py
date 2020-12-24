class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head # create a dummy variable that stands before head
        curr = dummy # curr becomes a dummy var
        while curr.next:
            if curr.next.val == val: # if the next node is the number we want to remove
                curr.next = curr.next.next # relinking one node forward
            else:
                curr = curr.next # otherwise keep moving 
        return dummy.next


    def removeElements_easy(self, head, val):
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


    def removeElements_another(self, head, val):
        if not head: return
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev and head:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
                else:
                    head = head.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
        return head


    def removeElements_recursive(self, head, val):
        def _helper(node, val):
            if node:
                if node.val == val:
                    return _helper(node.next, val)
                else:
                    node.next = _helper(node.next, val)
            return node
        return _helper(node, val)
        

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(6)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)
    l.next.next.next.next.next = ListNode(5)
    l.next.next.next.next.next.enxt = ListNode(5)
    print(l.removeElements_another(l, 6))

