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


def getIntersectionNode(headA, headB): # O(length_a + length_b) and O(1)
    """
    calculate the lengths of both lists
    Calculate the difference in length as length of longer - length of shorter
    Move the pointer pointing to the head of the longer by the difference
    Now you have two pointers in way so that the number of elements to the right from them is equal
    Traverse in parallel, if found equal, return 
    """
    length_a, length_b = 0, 0
    curr_a, curr_b = headA, headB
    while curr_a:
        curr_a = curr_a.next
        length_a += 1
    while curr_b:
        curr_b = curr_b.next
        length_b += 1
    curr_a, curr_b = headA, headB
    if length_a > length_b:
        diff = length_a - length_b
        while diff > 0:
            curr_a = curr_a.next
            diff -= 1
    else:
        diff = length_b - length_a
        while diff > 0:
            curr_b = curr_b.next
            diff -= 1
    while curr_a:
        if curr_a == curr_b:
            return curr_a
        curr_a = curr_a.next
        curr_b = curr_b.next
    return None


