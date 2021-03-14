# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseBetween(self, head, m, n):
        if not head:
            return
        zero = ListNode(-1)
        zero.next = head

        prev, curr = zero, zero.next
        for _ in range(1, m):
            prev = curr
            curr = curr.next
        for _ in range(n - m):
            next_n = curr.next
            curr.next = next_n.next
            next_n.next = prev.next
            prev.next = next_n
        return zero.next
    
    def reverseBetween_another(self, head, m, n):
        if not head or not head.next: return head
        if m == n: return head
        # handle m == 1 case
        counter = 0
        curr = ListNode(0)
        curr.next = head
        head = curr
        # traverse up to the (m-1)th node
        while counter < m - 1 and curr:
            counter += 1
            curr = curr.next
        # assign m-1th node
        frontHeadNode = curr
        curr = curr.next    #mth node
        counter += 1
        mthNode = curr
        prev = endNode = None
        # start from mth node up to nth node
        while curr and counter <= n:    # do traditional reversal of LL
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if counter == n:    # when counter == n, grab the next value and break
                endNode = curr if curr else None
                break
            counter += 1
        # connect the reversed LL into original
        frontHeadNode.next = prev
        mthNode.next = endNode
        return head.next
