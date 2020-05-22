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

    class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        visited = set()
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next
        return None
