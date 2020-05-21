class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break

        if p2 is None or p2.next is None:
            return None

        p1 = head
        while p2 is not p1:
            p2 = p2.next
            p1 = p1.next

        return p2
