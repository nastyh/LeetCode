# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
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
