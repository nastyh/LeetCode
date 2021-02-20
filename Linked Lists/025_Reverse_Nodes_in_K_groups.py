def reverseKGroup(self, head: ListNode, k: int) -> ListNode:  # O(n) and O(1)
    def reverse_list(node, end):
        prev = None
        tail = node
        while node != end:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev, tail
    
    dummy = node = ListNode(0, head)
    count = 0
    while head:
        if count == k:
            node.next, tail= reverse_list(node.next, head)
            node = tail
            count = 0
            tail.next = head                
        head = head.next
        count += 1
    if count == k:
        node.next, tail= reverse_list(node.next, head)
        tail.next = head         
    return dummy.next


def reverseKGroup_alt(head, k):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        next = curr.next
        curr.next = None
        curr = next
    
    if len(nodes) < k:
        return head
    
    prev = None
    flag = False
    for i in range(1, len(nodes)):
        if i % k != 0:
            nodes[i].next = nodes[i - 1]
        elif (i + k - 1) < len(nodes):
            nodes[i - k].next = nodes[i + k - 1]
        else:
            nodes[i - k].next = nodes[i]
            flag = True
            break
    if flag:
        for i in range(len(nodes) - len(nodes) % k, len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
    return nodes[k - 1]


def reverseKGroup_recursion(head, k): # O(n) and O(k) b/c of the recursion stack
    dumb_head = pointer = ListNode()
    pointer.next = head
    def _reverseSubGroup(head_pointer, last_pointer, num):
        if num == 0:
            return head_pointer, last_pointer, True
        if num > 0 and last_pointer is None:
            return None, None, False
        if num > 0:
            h, l, is_changed = _reverseSubGroup(head_pointer, last_pointer.next, num - 1)
            if is_changed:
                next_node = h.next
                h.next = l
                return next_node, h, True
            else:
                return None, None, False
    is_changed = True
    while is_changed and pointer is not None:
        h, l, is_changed = _reverseSubGroup(pointer.next, pointer.next, k)
        if is_changed:
            next_pointer = pointer.next
            pointer.next = l
            pointer = next_pointer
        
    return dumb_head.next