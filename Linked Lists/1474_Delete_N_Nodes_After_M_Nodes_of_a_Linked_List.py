def deleteNodes(self, head, m, n):
    prev, curr = head, head
    while curr:
        m_counter, n_counter = m, n
        while curr and m_counter != 0:
            prev = curr
            curr = curr.next
            m_counter -= 1
            
        while curr and n_counter != 0:
            curr = curr.next
            n_counter -= 1
        prev.next = curr
    return head