def getIntersectionNode(headA, headB): # using extra space
d_a = {}
    curr = headA
    while curr:
        d_a[curr] = curr.val
        curr = curr.next

    curr_b = headB
    while curr_b:
        if curr_b in d_a:
            return curr_b
        curr_b = curr_b.next
    return None

def getIntersectionNode(headA, headB): # without extra_space

    hA = headA
    hB = headB
    A = 0 #len of headA
    while headA:
        A += 1
        headA = headA.next
    B = 0 #len of headB
    while headB:
        B += 1
        headB = headB.next
    diff = A-B #difference
    while diff>0:
        hA = hA.next
        diff -= 1
    while diff<0:
        hB = hB.next
        diff += 1
    while hA != hB:
        hA = hA.next
        hB = hB.next
    return hA


