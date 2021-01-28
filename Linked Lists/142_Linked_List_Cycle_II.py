def detectCycle(head):  # O(n) and O(1)
    """
    use slow and fast pointers: slow which moves one step at a time and fast, which moves two times at a time.
    To find the place where loop started, we need to do it in two iterations: first we wait until fast pointe
    gains slow pointer and then we move slow pointer to the start and run them with the same speed and wait
    until they concide.
    """
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
