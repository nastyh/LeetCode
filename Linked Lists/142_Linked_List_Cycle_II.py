def detectCycle(head):
    if not head: return None
    if head and not head.next: return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    
    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return slow


def detectCycle_alt(head):
    cur = head
    visited = set()
    while cur:
        if cur in visited:
            return cur
        visited.add(cur)
        cur = cur.next
    return None
