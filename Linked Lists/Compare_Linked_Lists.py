def compareLists(node1, node2):
    i = 0; j = 0
    while node1 and node2:
        while i < len(node1.val) and j < len(node2.val):
            if node1.val[i] != node2.val[j]:
                return False
            i += 1
            j += 1
        
        if i == len(node1.val):
            i = 0
            node1 = node1.next
        
        if j == len(node2.val):
            j = 0
            node2 = node2.next
    return node1 is None and node2 is None