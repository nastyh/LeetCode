# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = dummy = ListNode(-1)
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            l3.next = ListNode(value)
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            l3.next = ListNode(1)
        return dummy.next

    
    def addTwoNumbers_alt(self, l1, l2):
        """
        Slighty different in the main loop: while l1 and l2 
        It finishes looping once we are done with a shorter list.
        We still have to process a longer one
        And if after all of that we still have a carry, add an extra 1
        """
        if not l1 and not l2: return
        if l1 and not l2: return l1
        if not l1 and l2: return l2
        l3 = dummy = ListNode(-1)
        carry = 0
        while l1 and l2:
            num = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l3.next = ListNode(num)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            num = carry + l1.val
            carry = num // 10
            l3.next = ListNode(num % 10)
            l3 = l3.next
            l1 = l1.next
        while l2:
            num = carry + l2.val
            carry = num // 10
            l3.next = ListNode(num % 10)
            l3 = l3.next
            l2 = l2. next
        if carry != 0:
            l3.next = ListNode(1)
        return dummy.next 
        


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next = ListNode(4)
    res = ListNode()

    print(res.addTwoNumbers(l1, l2))


