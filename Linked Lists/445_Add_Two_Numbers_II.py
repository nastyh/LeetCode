# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):  # O(N1 + N2) and O(1)
    def _rev_helper(node):  # reverse a linked list
        if not node: return
        prev, curr = None, node
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n 
        return prev
    
    l3 = _rev_helper(l1)
    l4 = _rev_helper(l2)
    l5 = dummy = ListNode(-1)
    carry = 0
    while l3 or l4:  # important to do with or. With "and" will be hard to propagate further 
        val3 = l3.val if l3 else 0
        val4 = l4.val if l4 else 0
        value = (val3 + val4 + carry) % 10
        carry = (val3 + val4 + carry) // 10
        l5.next = ListNode(value)
        l5 = l5.next
        l3 = l3.next if l3 else None
        l4 = l4.next if l4 else None
    if carry:
        l5.next = ListNode(1)
    return _rev_helper(dummy.next)


def addTwoNumbers_no_reverse(self, l1, l2):  # O(N1 + N2) and O(1)
    """
    Follow-up w/o reversing lists
    """
    n1 = n2 = 0
    while l1:
        n1 *= 10
        n1 += l1.val
        l1 = l1.next
    while l2:
        n2 *= 10
        n2 += l2.val
        l2 = l2.next
    n3 = n1 + n2        
    
    ##turn n3 to linked list
    prev = ListNode(-1)
    head = prev
    for i in str(n3):
        n = ListNode(i)
        head.next = n
        head = n
    return prev.next


def addTwoNumbers_deque(self, l1, l2):
    q1 = collections.deque()
    q2 = collections.deque()
    while l1 or l2:
        if l1 and l2:
            q1.append(l1.val)
            q2.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            q1.append(l1.val)
            q2.appendleft(0)
            l1 = l1.next
        else:
            q1.appendleft(0)
            q2.append(l2.val)
            l2 = l2.next
    carry = 0
    cur = None
    while q1 and q1:
        n1, n2 = q1.pop(), q2.pop()
        if n1 + n2 + carry >= 10:
            cur = ListNode(n1 + n2 + carry - 10, cur)
            carry = 1
        else:
            cur = ListNode(n1 + n2 + carry, cur)
            carry = 0
    if carry == 1:
        return ListNode(1, cur)
    else:
        return cur
        
def addTwoNumbers_stack(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        extra q: without reversing explicitly (only the answer)
        O(max(m, n))  -- the longer of the two lists
        O(m + n) -- due to the stack
        """
        def _helper_reverse_result(node):
            prev = None
            curr = node
            while curr:
                next_n = curr.next
                curr.next = prev 
                prev = curr
                curr = next_n
            return prev 
       
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0
            curr_val = (v1 + v2 + carry)
            carry = curr_val // 10
            curr_val = curr_val % 10
            curr.next = ListNode(curr_val)
            curr = curr.next 
        if carry:
            curr.next = ListNode(1)
        # return dummy.next
        return _helper_reverse_result(dummy.next)
        
