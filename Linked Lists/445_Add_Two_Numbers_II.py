# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def _rev_helper(node):
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
    while l3 or l4:
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
        
