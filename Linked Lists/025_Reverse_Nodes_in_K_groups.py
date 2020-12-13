def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
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